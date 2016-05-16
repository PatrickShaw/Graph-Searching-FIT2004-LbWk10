import random

import sys
import threading

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
            :complexity: O(m²ⁿ) Which relates to the total number of edges.
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
                # print(len(v.edges))
                v.edges.append(connected_vertex_index)
                connected_vertex_index += 1
                connected_vertex_index %= initial_vertex_count
        # Good we're done setting up d graph, run the super class constructor
        super().__init__(vertices)

    @property
    def m(self):
        """
            :returns: The number of different letters that can be used in each vertex's associated string
        """
        return self.__m

    @property
    def n(self):
        """
            :returns: The number of letters associated with each vertex
        """
        return self.__n

    @property
    def initial_vertex_len(self):
        """
            :returns: The initial number of vertices in the D graph
        """
        return self.m ** self.n

    @property
    def initial_edges_per_vertex(self):
        """
            :returns: The initial number of edges per vertex in the D graph
        """
        return self.m

    @property
    def initial_total_edge_len(self):
        """
            :returns: The number of edges originally in each
        """
        return self.initial_vertex_len * self.initial_edges_per_vertex


def convert_base(width, n, base):
    convert_string = "ABCDE"
    if n < base:
        return pad_left(convert_string[n], width)
    else:
        return pad_left(convert_base(width, n // base, base) + convert_string[n % base], width)


def pad_left(string, width):
    while len(string) < width:
        string = 'A' + string
    return string


def number_to_letter(char):
    if char == 0:
        return 'A'
    elif char == 1:
        return 'B'
    elif char == 2:
        return 'C'
    elif char == 3:
        return 'D'


def main():
    sys.setrecursionlimit(2000000000)
    threading.stack_size(200000000)
    m = range_input("Enter m", 2, 5)
    n = range_input("Enter n", 2, 8)
    import time
    graph = DGraph(m, n)
    start_time = time.time()
    e_circuit = graph.e_circuit
    print(time.time() - start_time)
    if e_circuit is not None:
        print("E circuit found!")
        print(convert_base(n, e_circuit[0], m) + "".join(
            [convert_base(n, e_circuit[x], m)[-1] for x in range(1, len(e_circuit))]))
    else:
        print("E circuit not found!")

    print(e_circuit)


if __name__ == "__main__":
    main()
