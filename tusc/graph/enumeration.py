import networkx as nx
import numpy as np


def count_spanning_trees(G):
    """
    Employs Matrix-Tree Thm to count the spanning trees of a graph.

    Parameters
    ----------
    G : NetworkX graph

    References
    ----------
    [1] Kirchhoff's theorem. Wikipedia. Retrieved from
    https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem.
    """
    Q = nx.laplacian_matrix(G).toarray()
    Q_star = Q[:-1,:-1]
    return round(np.linalg.det(Q_star))

def count_loops(G):
    """
    Count the loop edges in a graph.

    Parameters
    ----------
    G : NetworkX graph
    """
    loops = get_loops(G)
    return len(loops)

def get_loops(G):
    """
    Returns the loop edges in a graph.

    Parameters
    ----------
    G : NetworkX graph
    """
    return [e for e in G.edges if e[0] == e[1]]

def count_cut_edges(G):
    """
    Count the loop edges in a graph.

    Parameters
    ----------
    G : NetworkX graph
    """
    loops = get_cut_edges(G)
    return len(loops)

def get_cut_edges(G):
    """
    Returns the cut-edges in a graph.

    Parameters
    ----------
    G : NetworkX graph
    """
    cut_edges = []
    for e in G.edges:
        G_copy = G.copy()
        G_copy.remove_edge(*e)
        if len(list(nx.connected_components(G_copy))) > 1:
            cut_edges.append(e)
    return cut_edges
