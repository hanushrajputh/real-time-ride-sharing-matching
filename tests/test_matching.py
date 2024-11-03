import unittest
from src.matching import Matcher

class TestMatcher(unittest.TestCase):
    def setUp(self):
        self.matcher = Matcher()
        self.matcher.add_driver("driver1", (40.7128, -74.0060))
        self.matcher.add_driver("driver2", (40.7306, -73.9352))

    def test_match_rider(self):
        matched_driver = self.matcher.match_rider((40.748817, -73.985428))
        self.assertEqual(matched_driver, "driver1")
