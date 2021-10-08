import networkx as nx
import numpy as np

def multiply_edges(G, k):
    """
    Creates a new graph G_prime with k copies of each edge in G

    Parameters
    ----------
    G : networkx graph
        source graph
    k : int
        the number of edge copies

    Returns
    -------
    G_prime : networkx graph
        new graph
    """
    G_prime = nx.MultiGraph()
    for edge in G.edges:
        for i in range(k):
            G_prime.add_edge(edge[0], edge[1])
    return G_prime

def pathify_edges(G, k):
    """
    Creates a new graph G_prime where each edge in G is replaced with a path of
    length k through k-1 new vertices.

    Parameters
    ----------
    G : networkx graph
        source graph
    k : int
        path length

    Returns
    -------
    G_prime : networkx graph
        new graph
    """
    G_prime = nx.Graph()
    for edge in G.edges:
        for counter in range(k):
            if counter == 0:
                G_prime.add_edge(
                    edge[0],
                    str(edge)+"_"+str(counter)
                )
            elif counter == k-1:
                G_prime.add_edge(
                    str(edge)+"_"+str(counter-1),
                    edge[1]
                )
            else:
                G_prime.add_edge(
                    str(edge)+"_"+str(counter-1),
                    str(edge)+"_"+str(counter)
                )
    return G_prime
