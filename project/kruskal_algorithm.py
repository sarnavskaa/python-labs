import time
from typing import List


# class which is representing edge between vertices
class Edges:

    # initializing vertex a and vertex b which are joined with w - weight
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.weight = w

    def __repr__(self):
        return f"Edge({str(self.a)}, {str(self.b)}, {str(self.weight)})"

    def __str__(self):
        return f"{str(self.a)} - {str(self.b)} weight: {str(self.weight)}"


# class contains necessary methods of algorithm
class KruskalAlgorithm:

    def __init__(self, file_name='graph.txt'):
        self.graph: List[Edges] = []

        # loading graph from file and extraction of vertices and edges number
        self.number_of_vertices, self.number_of_edges = self.load_graph(file_name)
        self.parents = self.load_dependency()

    # load graph from graph.txt file by default and fill array of vertices
    def load_graph(self, file):
        file = open(file, "rt")
        vertices = set()
        # create graph data structure with vertex 1 (a) vertex 2 (b) and weight
        for line in file:
            a, b, weight = (line.split())
            self.graph.append(Edges(int(a), int(b), int(weight)))
            vertices.add(a), vertices.add(b)

        file.close()
        self.graph.sort(key=lambda w: w.weight)
        return len(vertices), len(self.graph)

    # method to fill array of parents with is representing dependency between vertices
    def load_dependency(self):
        return [vertex for vertex in range(self.number_of_vertices + 1)]

    # method to find if vertices have the same parents
    def find_parents(self, x):
        if self.parents[x] == x:
            return x
        return self.find_parents(self.parents[x])

    # join vertices if they haven't the same parents, in that way one of them is a parent of another one
    def join(self, x, y):
        find_x, find_y = self.find_parents(x), self.find_parents(y)
        if find_x != find_y:
            self.parents[find_x] = find_y

    # main method to execute algorithm
    def run(self):
        min_spanning_tree: List[Edges] = []

        for edge in range(len(self.graph)):
            a = int(self.graph[edge].a)
            b = int(self.graph[edge].b)
            weight = int(self.graph[edge].weight)

            # check if two vertices can create a cycle and if they can't - join them
            if algorithm.find_parents(a) != algorithm.find_parents(b):
                algorithm.join(a, b)
                # addition of edge to spanning tree
                min_spanning_tree.append(Edges(a, b, weight))

        return min_spanning_tree


if __name__ == '__main__':
    algorithm = KruskalAlgorithm()

    print('\nLoaded graph:\n')
    [print(str(algorithm.graph[edge])) for edge in range(len(algorithm.graph))]

    # run algorithm and get minimum spanning tree and check time
    t1 = time.perf_counter()
    minimum_spanning_tree: List[Edges] = algorithm.run()
    t2 = time.perf_counter()
    time_diff = t2 - t1

    print(f'\nMinimum spanning tree found with Kruskal Algorithm in {time_diff:.5f} secs:\n')
    [print(str(minimum_spanning_tree[edge])) for edge in range(len(minimum_spanning_tree))]
