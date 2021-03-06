import unittest
from project.kruskal_algorithm import *


class TestEdges(unittest.TestCase):

    def setUp(self):
        self.edge1 = Edges(1, 2, 3)
        self.edge2 = Edges(10, 7, 5)
        self.edge3 = Edges(0, 1, 4)

    def test___str__(self):
        self.assertEqual("1 - 2 weight: 3", str(self.edge1))
        self.assertEqual("10 - 7 weight: 5", str(self.edge2))
        self.assertEqual("0 - 1 weight: 4", str(self.edge3))

    def test___repr__(self):
        self.assertEqual("Edge(1, 2, 3)", repr(self.edge1))
        self.assertEqual("Edge(10, 7, 5)", repr(self.edge2))
        self.assertEqual("Edge(0, 1, 4)", repr(self.edge3))

    def tearDown(self):
        self.edge1 = None
        self.edge2 = None
        self.edge3 = None


class TestKruskalAlgorithm(unittest.TestCase):

    def setUp(self):
        self.test1 = KruskalAlgorithm('graphs/test1.txt')
        self.test2 = KruskalAlgorithm('graphs/test2.txt')
        self.graph = KruskalAlgorithm()

    def load_results(self):

        self.min_spanning_tree_test1: List[Edges] = [Edges(1, 2, 1),
                                                     Edges(2, 5, 1),
                                                     Edges(2, 4, 2),
                                                     Edges(3, 6, 2),
                                                     Edges(1, 3, 2)]

        self.min_spanning_tree_test2: List[Edges] = [Edges(1, 4, 5),
                                                     Edges(3, 5, 5),
                                                     Edges(4, 6, 6),
                                                     Edges(1, 2, 7),
                                                     Edges(2, 5, 7),
                                                     Edges(5, 7, 9)]

        self.min_spanning_tree_graph: List[Edges] = [Edges(1, 3, 1),
                                                     Edges(4, 5, 2),
                                                     Edges(1, 2, 3),
                                                     Edges(2, 4, 5)]

    def test_load_graph(self):
        self.assertEqual((6, 7), self.test1.load_graph('graphs/test1.txt'))
        self.assertEqual((7, 11), self.test2.load_graph('graphs/test2.txt'))
        self.assertEqual((5, 7), self.graph.load_graph('graphs/graph.txt'))

    def test_load_dependency(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6], self.test1.load_dependency())
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], self.test2.load_dependency())
        self.assertEqual([0, 1, 2, 3, 4, 5], self.graph.load_dependency())

    def test_join(self):
        self.test1.join(1, 2)
        self.test2.join(1, 4)
        self.graph.join(1, 3)
        self.assertEqual([0, 2, 2, 3, 4, 5, 6], self.test1.parents)
        self.assertEqual([0, 4, 2, 3, 4, 5, 6, 7], self.test2.parents)
        self.assertEqual([0, 3, 2, 3, 4, 5], self.graph.parents)

    def test_run(self):
        self.load_results()
        self.assertEqual(str(self.min_spanning_tree_test1), str(self.test1.run()))
        self.assertEqual(str(self.min_spanning_tree_test2), str(self.test2.run()))
        self.assertEqual(str(self.min_spanning_tree_graph), str(self.graph.run()))

        self.min_spanning_tree_test1 = None
        self.min_spanning_tree_test2 = None
        self.min_spanning_tree_graph = None

    def test_find_parents(self):
        self.test_run()

        self.assertEqual(6, self.test1.find_parents(self.test1.graph[1].a))
        self.assertEqual(7, self.test2.find_parents(self.test2.graph[1].a))
        self.assertEqual(5, self.graph.find_parents(self.graph.graph[1].a))

    def tearDown(self):
        self.test1 = None
        self.test2 = None
        self.graph = None


if __name__ == '__main__':
    unittest.main()
