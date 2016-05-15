from d_graph import *
__author__ = "Patrick Shaw"


def has_outgoing_edges(vertex):
    return len(vertex) > 0


def would_disconnect(graph, current_vertex_index, current_edge_index, target_vertex):
    #graph = list(graph)
    """
        Breadth First Search
        For all intents in purposes if we can get back to the original vertex then it's still connected
        since all we did was remove a single edge
        :complexity: Big O complexity = O(|V| + |E|)
                     Technically every edge and vertex could be explored to find the target_vertex
        :param graph: The graph
        :param current_vertex: The current vertex we are traversing from
        :param current_edge_index: Index of the edge that we are going to traverse through
        :param target_vertex: The vertex that we are searching for
    """
    next_vertex_index = graph[current_vertex_index[current_edge_index]]
    print(graph)
    print("Current vertex edges: " + str(len(current_vertex)))
    print("Current edge index: " + str(current_edge_index))
    print("Next vertex index: " + str(next_vertex_index))
    next_vertex = graph[next_vertex_index]
    # if we're on the same vertex we're good!
    if next_vertex == current_vertex:
        #print("Connected! 1")
        return True
    del current_vertex[current_edge_index]
    # Okay so we consumed the edge
    next_edge_len = len(next_vertex)
    for i in range(next_edge_len):
        if not would_disconnect(graph, next_vertex, i, target_vertex):
            current_vertex.insert(current_edge_index, next_vertex_index)
            #print("Connected 2!")
            return True
    # Add the vertex back in
    current_vertex.insert(current_edge_index,next_vertex_index)
    #print("Not connected!")
    return False


def e_circuit(graph, m, n, starting_vertex):
    """
        Consumes the graph in the process
        :complexity: Big O complexity = O(V^4) or O(|E|*(|V| + |E|))
                     BFS is O(|V| + |E|) or O(|V|^2).
                     We need to perform BFS each time we traverse and we traverse through the number of edges (thus, |E*(|V| + |E|))
                     Since |E| can be at most |V|^2 we can write it as
                     O(|V|^4)
        :return:
        if we didn't find an e circuit: None
        if we found an e circuit: a deque of the vertex indexes we went to
    """
    current_vertex = starting_vertex
    untraversed_edges = d_graph_edge_len(m, n)
    vertices_traversed = []
    # Will end if we finally got round to every vertex
    while(untraversed_edges > 0):
        print("---------------------------------------------------------------")
        print(graph)
        # Didn't find a circuit
        if not has_outgoing_edges(current_vertex):
            return None
        # Just select the first edge by default
        current_vertex_selected_edge_index = 0
        # Oh! We have more than one edge
        # let's try find an appropriate edge
        if len(current_vertex) > 0:
            old_edge_len = len(current_vertex)
            for i in range(old_edge_len):
                # Delete the edge but add it back in after we perform the check
                if not would_disconnect(graph, current_vertex, i, current_vertex):
                    current_vertex_selected_edge_index = len(current_vertex) - 1
                    break
        next_vertex_index = current_vertex[current_vertex_selected_edge_index]
        # We just consumed the edge so get rid of it
        print(current_vertex[current_vertex_selected_edge_index])
        vertices_traversed.append(current_vertex[current_vertex_selected_edge_index])

        del current_vertex[current_vertex_selected_edge_index]
        print(next_vertex_index)
        untraversed_edges -= 1
        current_vertex = graph[next_vertex_index]
    return vertices_traversed
