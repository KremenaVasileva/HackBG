from directed_graph import DirectedGraph
import unittest


class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.nodeA = "A"
        self.nodeB = "B"
        self.nodeC = "C"
        self.nodeD = "D"
        self.nodeE = "E"

    def test_init(self):
        self.assertTrue(isinstance(self.graph, DirectedGraph))

    def test_add_node(self):
        self.graph.add_node(self.nodeA)
        self.assertTrue(self.nodeA in self.graph.nodes)

    def test_add_edge(self):
        self.graph.add_edge(self.nodeA, self.nodeB)
        self.assertTrue(self.nodeB in self.graph.nodes[self.nodeA])

    def test_get_neighbours_for(self):
        self.graph.add_edge(self.nodeB, self.nodeC)
        self.graph.add_edge(self.nodeB, self.nodeD)
        friends_of_nodeB = [self.nodeC, self.nodeD]
        self.assertTrue(friends_of_nodeB == self.graph.nodes[self.nodeB])

    def test_path_between(self):
        self.graph.add_edge(self.nodeA, self.nodeB)
        self.graph.add_edge(self.nodeB, self.nodeC)
        self.graph.add_edge(self.nodeB, self.nodeD)
        self.graph.add_edge(self.nodeD, self.nodeA)

        self.assertTrue(self.graph.path_between(self.nodeA, self.nodeD))
        self.assertFalse(self.graph.path_between(self.nodeA, self.nodeE))


if __name__ == '__main__':
    unittest.main()
