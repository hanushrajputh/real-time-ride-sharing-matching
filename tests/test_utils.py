import unittest
from src.geohashing import GeoHashing  # Import GeoHashing instead of calculate_distance directly

class TestUtils(unittest.TestCase):
    def test_calculate_distance(self):
        distance = GeoHashing.calculate_distance((40.7128, -74.0060), (40.7306, -73.9352))  # Use the static method from GeoHashing
        self.assertAlmostEqual(distance, 1.5, delta=0.1)  # Adjust this value according to the actual distance
