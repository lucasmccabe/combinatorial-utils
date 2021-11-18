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
        >>> print(tutte_C5.polynomial)
        'x**4 + x**3 + x**2 + x + y'
        >>> tutte_C5.evaluate(2, 0)
        30

    Get the Tutte polynomial for the diamond graph:

        >>> G = nx.diamond_graph()
        >>> tutte_G = cz.graph.polynomial.Tutte(G)
        >>> print(tutte_G.polynomial)
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
        Generates the Tutte polynomial for the provided graph via recursion
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
        D = G.copy()
        D.remove_edge(*e) # delete
        C = manipulation.contract_edge(G, e) # contract
        #C = nx.contracted_edge(G, e, self_loops = False)
        return self._generate_polynomial(D) + self._generate_polynomial(C)

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

class Chromatic():
    """
    For computing and evaluating the chromatic polynomial of a graph.

    Example Usage
    -------------
    Get the chromatic polynomial for C_5, and calculate the number of 3-colorings:

        >>> C5 = nx.cycle_graph(5)
        >>> tutte_C5 = cz.graph.polynomial.Tutte(C5)
        >>> print(tutte_C5.polynomial)
        'x**5 - 5*x**4 + 10*x**3 - 10*x**2 + 4*x'
        >>> tutte_C5.evaluate(3)
        30

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
        self.polynomial = self.generate_polynomial()

    def generate_polynomial(self, G = None):
        """
        Generates the chromatic polynomial for the provided graph via recursion
        and deletion-contraction.

        Parameters
        ----------
        G : NetworkX graph
        """
        if not G:
            G = self.G

        if len(G.edges) == 0:
            return self.x**len(G.nodes)
        if len(G.nodes) == 1:
            return self.x

        # pick an edge arbitrarily
        e = random.choice(list(G.edges))
        # deletion-contraction
        D = G.copy()
        D.remove_edge(*e) # delete
        C = nx.contracted_edge(G, e, self_loops = False) # contract w/o loops
        return self.generate_polynomial(D) - self.generate_polynomial(C)

    def evaluate(self, x):
        """
        Evaluates the chromati polynomial for the graph, given x, to find the
        number of x-colorings of the graph.

        Parameters
        ----------
        x : float
            coloring number
        """
        result = self.polynomial.subs([(self.x, x)])
        if type(x) == int:
            return int(result)
        if type(x) == float:
            return float(result)
        else:
            raise ValueError("Unknown result type error.")
