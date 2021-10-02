import networkx as nx
import numpy as np


def spanning_trees(G):
    """
    Employs Matrix-Tree Thm to count the spanning trees of a graph.

    Parameters
    ----------
    G : a networkx graph
    """
    Q = nx.laplacian_matrix(G).toarray()
    Q_star = Q[:-1,:-1]
    return round(np.linalg.det(Q_star))
