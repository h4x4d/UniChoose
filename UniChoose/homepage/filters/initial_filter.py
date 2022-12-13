from departments.models import Department
from homepage.filters.distance_filter import distance_checker
from homepage.filters.subjects_filter import departments_checker
from universities.models import Region, University


def initial_filter(user):
    regions = Region.objects.all()

    regions = [region for region in regions if distance_checker(user, region)]
    universities = University.objects.filter(region__in=regions)

    user_subjects = user.subjects.all()
    user_marks = [subject.mark for subject in user_subjects]
    user_subjects = [subject.name for subject in user_subjects]

    departments = []
    for department in Department.objects.filter(university__in=universities):
        if departments_checker(user_subjects, user_marks, department):
            departments.append(department)

    return departments
