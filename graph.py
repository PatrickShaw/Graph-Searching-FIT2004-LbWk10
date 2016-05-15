from collections import deque
__author__ = "Patrick Shaw"


class Graph:
    """
        A class representing a graph that I can use if I choose to use this code in the future.
    """
    def __init__(self, vertices):
        """
            :param vertices: The vertices in the graph
        """
        self.__vertices = vertices

    @property
    def vertices(self):
        """
            :returns: Returns all the vertices in the graph
        """
        return self.__vertices

    def __del__(self):
        return NotImplemented

    def append(self, vertex):
        vertex.vertex_position = len(self.vertices)
        return self.vertices.append(vertex)

    def insert(self, index, vertex):
        return NotImplemented

    def __str__(self):
        return ("["+", ".join(str(v) for v in self.vertices)+"]").replace("deque(", "").replace(")],", "],")


class Vertex:
    """
        A class representing a vertex in a graph. Used to make life easier when dealing with the
        position of the vertex with linked lists and deque collections.
    """
    def __init__(self, vertex_position, edges=deque()):
        """
            :param vertex_position: Position of the vertex in the graph
            :param edges: The outgoing edges of the vertex
        """
        self.__vertex_position = vertex_position
        self.__edges = edges

    @property
    def edges(self):
        """
            :returns: All the outgoing edges connected to the vertex
        """
        return self.__edges

    @property
    def vertex_position(self):
        """
            :returns: The position of the vertex in the graph
        """
        return self.__vertex_position

    @property
    def has_outgoing_edges(self):
        """
            :returns: True if the vertex has outgoing edges, otherwise false.
        """
        return len(self.edges) > 0

    def __str__(self):
        return str(self.vertex_position)+":"+str(self.edges)
