from rest_framework import viewsets
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
        prefetch_related('university')
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

            departments = departments[:2]

        return Department.objects.filter(pk__in=departments)


class APILike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        relation = AccountDepartmentRelations()
        relation.account = request.user
        relation.department = Department.objects.get(pk=pk)
        relation.strength = 1
        relation.save()

        return Response({'success': True})


class APIDislike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        relation = AccountDepartmentRelations()
        relation.account = request.user
        relation.department = Department.objects.get(pk=pk)
        relation.strength = -1
        relation.save()

        return Response({'success': True})
