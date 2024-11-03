def calculate_distance(coord1, coord2):
    from geopy.distance import geodesic
    return geodesic(coord1, coord2).miles
