from annoy import AnnoyIndex

from departments.models import WeightedDepartment


def create_weighted_vector(data):
    return (float(data.entry_score) * 10, float(data.profile) * (10**-5),
            float(data.vuz_rating), float(data.edu_level) * 10)


def nearest_filter(departments, user, amount=2):
    u = AnnoyIndex(4, 'angular')
    preference = user.preference

    for department in WeightedDepartment.objects.filter(
            department__in=departments):

        u.add_item(department.id, create_weighted_vector(department))

    u.build(10)

    return u.get_nns_by_vector(create_weighted_vector(preference), amount)
