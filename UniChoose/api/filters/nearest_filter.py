from annoy import AnnoyIndex

from departments.models import WeightedDepartment


def nearest_filter(departments, user, amount=2):
    u = AnnoyIndex(4, 'angular')
    preference = user.preference

    for department in WeightedDepartment.objects.filter(
            department__in=departments):
        data = (float(department.entry_score) * 1,
                float(department.profile) * (10**-4),
                float(department.vuz_rating), float(department.edu_level) * 10)

        u.add_item(department.id, data)

    u.build(10)

    return u.get_nns_by_vector((preference.entry_score, preference.profile,
                                preference.vuz_rating, preference.edu_level),
                               amount)
