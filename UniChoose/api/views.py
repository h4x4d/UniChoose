from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters.initial_filter import initial_filter
from api.filters.nearest_filter import nearest_filter
from departments.models import Department
from departments.serializers import DepartmentSerializer
from users.models import AccountDepartmentRelations, Preference


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all().order_by('name'). \
        prefetch_related(Prefetch('university', to_attr='universities'))
    serializer_class = DepartmentSerializer

    permission_classes = [IsAuthenticated]


class PreferenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        departments = initial_filter(user)

        if user.preference:
            departments = nearest_filter(departments, user, 1)
        else:
            preference = Preference(
                entry_score=310,
                vuz_rating=10.0,
                edu_level=0,
                profile=0,
            )
            preference.save()
            user.preference = preference
            user.save()

            departments = nearest_filter(departments, user, 1)

        for department in departments:
            relation = AccountDepartmentRelations(account_id=user.id,
                                                  department_id=department,
                                                  strength=0)
            relation.save()

        return Department.objects.filter(pk__in=departments)


class APILike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        try:
            department = Department.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound()

        try:
            relation = AccountDepartmentRelations.objects.get(
                account=user, department=department)
        except ObjectDoesNotExist:
            raise PermissionDenied()

        relation.strength = 1
        relation.save()

        preference = user.preference

        if not preference:
            raise PermissionDenied()

        weighted = department.weighted

        if not weighted:
            raise NotFound()

        if preference.vuz_rating == 10.0:
            preference.vuz_rating = weighted.vuz_rating
            preference.entry_score = weighted.entry_score
            preference.edu_level = weighted.edu_level
            preference.profile = weighted.profile
            preference.user = user
        else:
            preference.vuz_rating = (weighted.vuz_rating +
                                     preference.vuz_rating) / 2
            preference.entry_score = (weighted.entry_score +
                                      preference.entry_score) / 2
            preference.edu_level = (weighted.edu_level +
                                    preference.edu_level) / 2
            preference.profile = weighted.profile
            preference.user = user
        preference.save()

        return Response({'success': True})


class APIDislike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user

        try:
            department = Department.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound()

        if not user.preference:
            raise PermissionDenied()

        try:
            relation = AccountDepartmentRelations.objects.get(
                account=user, department=department)
        except ObjectDoesNotExist:
            raise PermissionDenied()

        relation.strength = -1
        relation.save()

        return Response({'success': True})
