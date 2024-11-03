import unittest
from src.graph import RoadGraph

class TestRoadGraph(unittest.TestCase):
    def setUp(self):
        self.graph = RoadGraph()
        self.graph.add_location("A", (40.7128, -74.0060))
        self.graph.add_location("B", (40.7306, -73.9352))
        self.graph.add_road("A", "B", 1.5)

    def test_add_location(self):
        self.assertIn("A", self.graph.graph.nodes)
        self.assertIn("B", self.graph.graph.nodes)

    def test_add_road(self):
        self.assertIn(("A", "B"), self.graph.graph.edges)
