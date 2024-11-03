import unittest
from src.geohashing import GeoHashing  # Ensure this import points to the correct module

class TestGeoHashing(unittest.TestCase):
    def test_calculate_distance(self):
        # Coordinates for New York and a nearby location
        coord1 = (40.7128, -74.0060)  # New York City
        coord2 = (40.7306, -73.9352)  # Another location in NYC

        # Calculate distance using GeoHashing class
        distance = GeoHashing.calculate_distance(coord1, coord2)

        # Expected value should be updated based on the actual calculated distance
        expected_distance = 2.0  # Replace with the actual distance measured
        self.assertAlmostEqual(distance, expected_distance, delta=0.1)

if __name__ == '__main__':
    unittest.main()
