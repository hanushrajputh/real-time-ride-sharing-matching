import unittest
from src.utils import calculate_distance

class TestUtils(unittest.TestCase):
    def test_calculate_distance(self):
        distance = calculate_distance((40.7128, -74.0060), (40.7306, -73.9352))
        self.assertAlmostEqual(distance, 1.5, delta=0.1)
