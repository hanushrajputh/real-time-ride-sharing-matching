from src.geohashing import GeoHashing

class Matcher:
    def __init__(self):
        self.drivers = {}

    def add_driver(self, driver_id, location):
        self.drivers[driver_id] = location

    def match_rider(self, rider_location):
        closest_driver = None
        shortest_distance = float('inf')

        for driver_id, driver_location in self.drivers.items():
            distance = GeoHashing.calculate_distance(rider_location, driver_location)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_driver = driver_id

        return closest_driver
