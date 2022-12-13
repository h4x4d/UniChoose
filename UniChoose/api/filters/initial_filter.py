from api.filters.distance_filter import distance_checker
from api.filters.subjects_filter import departments_checker
from departments.models import Department
from universities.models import Region, University


def initial_filter(user):
    regions = Region.objects.all()

    regions = [region for region in regions if distance_checker(user, region)]
    universities = University.objects.filter(region__in=regions)

    user_subjects = user.subjects.all()
    user_marks = [subject.mark for subject in user_subjects]
    user_subjects = [subject.name for subject in user_subjects]
    user_id = user.id

    departments = []
    for department in Department.objects.filter(
            university__in=universities).order_by('entry_score',
                                                  'university__avg_rating'):
        if departments_checker(user_subjects, user_marks, user_id, department):
            departments.append(department)

    return departments
