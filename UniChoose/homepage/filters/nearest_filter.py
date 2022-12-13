from annoy import AnnoyIndex
from departments.models import WeightedDepartment


def nearest_filter(departments, user):
    u = AnnoyIndex(4, 'angular')
    preference = user.preference

    for department in WeightedDepartment.objects.filter(
            department__in=departments):
        u.add_item(department.id,
                   (float(department.entry_score) *
                    (10**-10), float(department.profile) *
                    (10**-10), float(department.vuz_rating) *
                    (10**-10), float(department.edu_level) * (10**-10)))

    u.build(10)

    return u.get_nns_by_vector((preference.entry_score, preference.profile,
                                preference.vuz_rating, preference.edu_level),
                               2)
