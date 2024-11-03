from geopy.distance import geodesic

class GeoHashing:
    @staticmethod
    def calculate_distance(coord1, coord2):
        return geodesic(coord1, coord2).miles
