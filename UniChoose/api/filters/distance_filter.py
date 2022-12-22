def distance_checker(user, university_region):
    if not user.region:
        return True
    return user.max_distance >= university_region.get_distance(user.region)
