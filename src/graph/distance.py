import networkx as nx
import numpy as np

def shortest_path(G, u, v, method = "Dijkstra"):
    """
    Calculates the shortest path between nodes u and v in G.

    Parameters
    ----------
    G : networkx graph
        source graph
    u : int or str - whatever type the labels of the graph are
        source node
    v : int or str - whatever type the labels of the graph are
        destination node
    method : str
        the shortest path method you want to use.
        Currently implemented:
            - "Dijkstra"
    """
    if method.lower() == "dijkstra":
        distances = single_source_shortest_paths(G, u, method = "Dijkstra")
        return distances[v]
    else:
        raise NotImplementedError

def single_source_shortest_paths(G, u, method = "Dijkstra"):
    """
    Calculates all shortest paths from node u and v in G.

    Parameters
    ----------
    G : networkx graph
        source graph
    u : int or str - whatever type the labels of the graph are
        source node
    method : str
        the shortest path method you want to use.
        Currently implemented:
            - "Dijkstra"
    """
    if method.lower() == "dijkstra":
        return _single_source_shortest_paths_dijkstra(G, u)
    else:
        raise NotImplementedError


def _single_source_shortest_paths_dijkstra(G, u):
    """
    Implements Dijkstra's algorithm for single-source shortest paths from u in G.

    Parameters
    ----------
    G : networkx graph
        source graph
    u : int or str - whatever type the labels of the graph are
        source node

    Notes
    -----
    [1] West, Douglas Brent. “Trees and Distance.” In Introduction to
    Graph Theory, 97–97. United States: Pearson, 2018.
    """
    G_old, u_old = G, u
    G = nx.convert_node_labels_to_integers(G_old)
    u = list(G_old.nodes).index(u)

    A = nx.adjacency_matrix(G)
    S = {u:0}
    T = {}
    for i in [j for j in G.nodes if j not in S]:
        if i not in G.neighbors(u):
            T[i] = np.inf
        else:
            T[i] = A[u, i]

    while len(S) < len(G):
        v = min(T, key = T.get)
        S[v] = T[v]
        T.pop(v)

        for i in [j for j in G.neighbors(v) if j not in S]:
            T[i] = min(T[i], S[v] + A[v, i])

    distances = {}
    for i in S:
        distances[list(G_old.nodes)[i]] = S[i]

    return distances
