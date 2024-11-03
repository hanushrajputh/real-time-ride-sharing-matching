import unittest
from src.geohashing import GeoHashing

class TestGeoHashing(unittest.TestCase):
    def test_calculate_distance(self):
        distance = GeoHashing.calculate_distance((40.7128, -74.0060), (40.7306, -73.9352))
        self.assertAlmostEqual(distance, 1.5, delta=0.1)
