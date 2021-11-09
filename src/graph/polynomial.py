import random
import networkx as nx
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
        'x^4 + x^3 + x^2 + x + y'
        >>> tutte_C5.evaluate(2, 0)
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
        polynomial = self._generate_polynomial(G)
        return self._simplify_polynomial(polynomial)

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

        if len(cut_edges) + len(loops) == len(G.edges):
            return "x^{c} y^{l}".format(
                c = str(len(cut_edges)),
                l = str(len(loops))
            )
        # pick an edge that isn't a cut edge or a loop
        e = [i for i in G.edges if i not in cut_edges and i not in loops][0]
        # deletion-contraction
        G_copy = G.copy()
        G_copy.remove_edge(*e)
        return "{delete} + {contract}".format(
            delete = self._generate_polynomial(G_copy),
            contract = self._generate_polynomial(
                manipulation.contract_edge(G, e)
            )
        )

    def _simplify_polynomial(self, polynomial):
        """
        Simplifies a Tutte polynomial string by combining like terms and
        handling exponents of 0 or 1.

        Parameters
        ----------
        polynomial : str
            the polynomial string you want to simplify
        """
        term_dict = {}
        terms = polynomial.split(" + ")
        for term in terms:
            if term in term_dict:
                term_dict[term] += 1
            else:
                term_dict[term] = 1
        polynomial = ""
        for term in term_dict:
            v = term_dict[term]
            term.replace("^1", "")
            if "0" in term or "1" in term:
                term_split = term.split(" ")
                if "^" in term_split[0]:
                    if term_split[0].split("^")[1] in ["0", "0 "]:
                        term_split[0] = ""
                if "^" in term_split[0]:
                    if term_split[0].split("^")[1] in ["1", "1 "]:
                        term_split[0] = term_split[0].split("^")[0]
                if "^" in term_split[1]:
                    if term_split[1].split("^")[1] in ["0", "0 "]:
                        term_split[1] = ""
                if "^" in term_split[1]:
                    if term_split[1].split("^")[1] in ["1", "1 "]:
                        term_split[1] = term_split[1].split("^")[0]
                term = "".join(term_split)

            if v == 1:
                polynomial += term + " + "
            else:
                polynomial += str(v) + " " + term + " + "

        return polynomial[:-3]

    def evaluate(self, x, y):
        """
        Evaluates the Tutte polynomial for the graph, given x, y.

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
            6
        """
        s = 0
        terms = self.polynomial.replace("^", "**").split(" + ")
        for term in terms:
            term_eval = eval(
                term.replace(
                    "x", "({x})".format(x = x)
                ).replace(
                    "y", "({y})".format(y = y)
                )
            )
            s += term_eval
        return s
