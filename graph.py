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
        self.vertices = vertices

    def __del__(self):
        return NotImplemented

    def append(self, vertex):
        vertex.vertex_position = len(self.vertices)
        return self.vertices.append(vertex)

    def insert(self, index, vertex):
        return NotImplemented

    def __str__(self):
        return ("["+", ".join(str(v) for v in self.vertices)+"]").replace("deque(", "").replace(")],", "],")

    def first_edge_is_bridge(self, current_vertex):
        return not self.depth_first_search(current_vertex, current_vertex, deque(), [False]*len(self.vertices))

    def depth_first_search(self, current_vertex, target_vertex, used_edge_stack, vertices_travelled_to):
        # If we've gone through a vertex and we've done all the searching of paths in that
        # vertex, why would we need to do it again? Answer: We don't, don't bother trying.
        if vertices_travelled_to[current_vertex.edges[0]]:
            return False
        #  Remember the next vertex's index
        next_vertex_index = current_vertex.edges.popleft()
        used_edge_stack.append(next_vertex_index)
        #  Cut off the edge so our algorithm doesn't use this edge again
        next_vertex = self.vertices[next_vertex_index]
        if next_vertex == target_vertex:
            # Good, looks like the vertex we traversed to was the vertex we're looking for
            # Gonna have to add that edge back in
            current_vertex.edges.appendleft(used_edge_stack.pop())
            return True
        # Darn, looks like the vertex isn't the one we're looking for
        # See if any of the vertices that it's connected to is the correct one
        for e in range(len(next_vertex.edges)):
            if self.depth_first_search(next_vertex, target_vertex, used_edge_stack, vertices_travelled_to):
                # Gonna have to add our edge edge back in
                current_vertex.edges.appendleft(used_edge_stack.pop())
                return True
        # Gonna have to add that edge back in
        # print("Did not find vertex")
        current_vertex.edges.appendleft(used_edge_stack.pop())
        vertices_travelled_to[next_vertex_index] = True
        return False


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
        self.edges = edges

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
