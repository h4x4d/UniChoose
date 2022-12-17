from api.filters.distance_filter import distance_checker
from api.filters.subjects_filter import departments_checker
from departments.models import Department
from universities.models import Region, University
from users.models import AccountDepartmentRelations
from django.db.models import Prefetch


def initial_filter(user):
    regions = Region.objects.all()

    regions = [region for region in regions if distance_checker(user, region)]
    universities = University.objects.filter(region__in=regions)

    user_subjects = user.subjects.all()
    user_marks = [subject.mark for subject in user_subjects]
    user_subjects = [subject.name for subject in user_subjects]
    user_id = user.id

    departments = []
    # department_queryset = (Department.objects
    #                        .filter(university__in=universities)
    #                        .order_by('entry_score', 'university__avg_rating')
    #                        .select_related('relations'))

    # queryset = (AccountDepartmentRelations.objects.select_related('department',
    #                                                               'account')
    #             .filter(department__university__in=universities)
    #             .order_by('department__entry_score',
    #                       'department__university__avg_rating'))

    queryset = (Department.objects
                .prefetch_related('relations')
                .filter(university__in=universities)
                .order_by('entry_score', 'university__avg_rating'))

    print(len(queryset))

    for department in queryset:
        print(department)
        if departments_checker(queryset, user_subjects, user_marks, user_id, department):
            departments.append(department)

    return departments
