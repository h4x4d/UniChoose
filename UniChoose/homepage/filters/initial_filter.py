from homepage.filters.distance_filter import distance_checker
from homepage.filters.subjects_filter import departments_checker
from universities.models import Region


def initial_filter(user):
    regions = Region.objects.all()

    regions = [region for region in regions if distance_checker(user, region)]

    universities = []
    for region in regions:
        universities += region.universities.all()

    departments = []
    user_subjects = user.subjects.all()
    user_marks = [subject.mark for subject in user_subjects]
    user_subjects = [subject.name for subject in user_subjects]

    for university in universities:
        for department in university.departments.all():
            if departments_checker(user_subjects, user_marks, department):
                departments.append(department)

    return departments
