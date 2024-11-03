import networkx as nx

class RoadGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_location(self, name, coordinates):
        self.graph.add_node(name, pos=coordinates)

    def add_road(self, from_node, to_node, distance):
        self.graph.add_edge(from_node, to_node, weight=distance)
