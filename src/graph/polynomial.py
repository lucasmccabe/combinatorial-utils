import random
import networkx as nx
import sympy
from . import enumeration, manipulation

class Tutte():
    """
    For computing and evaluating the Tutte polynomial of a graph.

    Example Usage
    -------------
    Get the Tutte polynomial for C_5 and use it to find the number of acyclic
    orientations of C_5:

        >>> C5 = nx.cycle_graph(5)
        >>> tutte_C5 = cz.graph.polynomial.Tutte(C5)
        >>> tutte_C5.polynomial
        'x**4 + x**3 + x**2 + x + y'
        >>> tutte_C5.evaluate(2, 0)
        30

    Get the Tutte polynomial for the diamond graph:

        >>> G = nx.diamond_graph()
        >>> tutte_G = cz.graph.polynomial.Tutte(G)
        >>> tutte_G.polynomial
        'x**3 + 2*x**2 + 2*x*y + x + y**2 + y'
    """
    def __init__(self, G):
        """
        Parameters
        ----------
        G : NetworkX graph

        """
        if G.is_directed():
            raise NotImplementedError
        self.G = G
        self.x = sympy.Symbol('x')
        self.y = sympy.Symbol('y')
        self.polynomial = self.generate_polynomial()

    def generate_polynomial(self, G = None):
        """
        Generates a simplified Tutte polynomial for the provided graph.

        Parameters
        ----------
        G : NetworkX graph
        """
        if not G:
            G = self.G
        return self._generate_polynomial(G)

    def evaluate(self, x, y):
        """
        Evaluates the Tutte polynomial for the graph, given x, y, using symbolic
        computation.

        Parameters
        ----------
        x : float

        y : float

        Example Usage
        -------------
        Count the # of acyclic orientations of G via T_G (2, 0):

            >>> G = nx.cycle_graph(5)
            >>> tutte = polynomial.Tutte(G)
            >>> tutte.evaluate(2, 0)
            30
        """
        result = self._evaluate_polynomial(x, y)
        if type(result) == sympy.core.numbers.Integer:
            return int(result)
        elif type(result) == sympy.core.numbers.Float:
            return float(result)
        else:
            raise ValueError("Unknown result type error.")

    def _generate_polynomial(self, G = None):
        """
        Generates the raw Tutte polynomial for the provided graph via recursion
        and deletion-contraction.

        Parameters
        ----------
        G : NetworkX graph
        """
        if not G:
            G = self.G
        # check base case
        cut_edges = enumeration.get_cut_edges(G)
        loops = enumeration.get_loops(G)
        some_edges = [i for i in G.edges if i not in cut_edges and i not in loops]

        #if len(cut_edges) + len(loops) == len(G.edges):
        if not some_edges:
            return self.x**len(cut_edges) * self.y**len(loops)
        # pick an edge that isn't a cut edge or a loop
        e = some_edges[0]
        # deletion-contraction
        d = G.copy()
        d.remove_edge(*e) # delete
        c = manipulation.contract_edge(G, e) # contract
        #c = nx.contracted_edge(G, e, self_loops = False)
        return self._generate_polynomial(d) \
            + self._generate_polynomial(c)

    def _evaluate_polynomial(self, x, y):
        """
        Evaluates the Tutte polynomial for the graph, given x, y, using symbolic
        computation.

        Parameters
        ----------
        x : float

        y : float
        """
        return self.polynomial.subs([(self.x, x), (self.y, y)])
