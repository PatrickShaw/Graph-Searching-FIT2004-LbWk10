import random

import sys

from int_input import range_input
from preconditions import preconditions
from graph import *
from collections import deque
__author__ = "Patrick Shaw"


class DGraph(Graph):
    @preconditions(
        lambda m: m >= 0 and isinstance(m, int),
        lambda n: n >= 0 and isinstance(n, int)
    )
    def __init__(self, m, n):
        """
            :param m: The base/different types of letters that graph can use for each vertex
            :param n: The number of letters associated with each vertex
            :returns: A D graph as a list
            :complexity: O(m²ⁿ)
                         We create mⁿ vertices and loop through them to add edges,
                         There are m edges for each vertex, thus
                         O(m²ⁿ)
        """
        self.__m = m
        self.__n = n
        initial_vertex_count = self.initial_vertex_len
        vertices = []
        for i in range(initial_vertex_count):
            vertices.append(Vertex(i, deque()))
        connected_vertex_index = 0
        # Go through all the vertices and add edges to them
        for v in vertices:
            # For each edge in the vertex
            for _ in range(m):
                #print(len(v.edges))
                v.edges.append(connected_vertex_index)
                connected_vertex_index += 1
                connected_vertex_index %= initial_vertex_count
        # Good we're done setting up d graph, run the super class constructor
        super().__init__(vertices)

    @property
    def m(self):
        """
            The number of different letters that can be used in each vertex's associated string
        """
        return self.__m

    @property
    def n(self):
        """
            The number of letters associated with each vertex
        """
        return self.__n

    @property
    def initial_vertex_len(self):
        """
            Returns the initial number of vertices in the D graph
        """
        return self.m**self.n

    @property
    def initial_edges_per_vertex(self):
        """
            Returns the initial number of edges per vertex in the D graph
        """
        return self.m

    @property
    def initial_total_edge_len(self):
        """
            Returns the number of edges originally in each
        """
        return self.initial_vertex_len * self.initial_edges_per_vertex


    @property
    def e_circuit(self):
        # "Start at any random vertex in the graph"
        current_vertex = self.vertices[0]  # random.choice(self.vertices)
        vertices_traversed = []
        untraversed_edge_count = self.initial_total_edge_len
        while untraversed_edge_count > 0:
            #print("---------------------------------------------------------")
            #print("On vertex position: " + str(current_vertex.vertex_position))
            #print(self)
            if untraversed_edge_count % 100 == 0:
                print(untraversed_edge_count)
            # Add this vertex to our traversal history
            vertices_traversed.append(current_vertex.vertex_position)
            # "the vertex has no outgoing edges... TERMINATE"
            if not current_vertex.has_outgoing_edges:
                #print("vertex has no outgoing edges, returning None")
                return None
            # "The vertex has two or more outgoing edges... Traverse along
            # edge... does NOT disconnect the vertex
            if len(current_vertex.edges) >= 1:
                for i in range(len(current_vertex.edges)):
                    #print("Checking if edge to: " + str(current_vertex.edges[i]) + " is a bridge")
                    if not self.first_edge_is_bridge(current_vertex):
                        #print(str(current_vertex.edges[0]) + " is not a bridge!")
                        # Break so that we can pop this of the start of the list
                        break
                    # We have to move the edge to the back of the queue since the algorithm only works with checking the first vertex
                    current_vertex.edges.append(current_vertex.edges.popleft())
            #print(self)
            next_vertex_index = current_vertex.edges.popleft()
            #print("Travelling to: " + str(next_vertex_index))
            current_vertex = self.vertices[next_vertex_index]
            untraversed_edge_count -= 1
        return vertices_traversed


def main():
    sys.setrecursionlimit(100000000)
    m = range_input("Enter m", 2, 5)
    n = range_input("Enter n", 2, 8)
    import time
    graph = DGraph(m, n)
    start_time = time.time()
    e_circuit = graph.e_circuit
    print(time.time() - start_time)
    print(e_circuit)
if __name__ == "__main__":
    main()
