import networkx as nx


class BipartitePreferences():
    """
    Holding class for example preference dictionaries.
    """
    def __init__(self, n, m):
        """

        Parameters
        ----------
        n : int
            left set size
        m : int
            right set size
        """
        self.n = n
        self.m = m


    def numerical_order(self):
        """
        Ranks each part in numerical order, e.g.
            {
                0 : [2, 3],
                1 : [2, 3],
                2 : [0, 1],
                3 : [0, 1]
            }
        """
        l_prefs = [i for i in range(self.n, self.n + self.m)]
        r_prefs = [i for i in range(self.n)]
        preferences = {}
        for i in range(self.n + self.m):
            if i < self.n:
                preferences[i] = l_prefs
            else:
                preferences[i] = r_prefs
        return preferences



class BipartiteMatching():
    def __init__(self, n, m, preferences = None):
        """
        Constructor for BipartiteMatching class.

        Parameters
        ----------
        n : int
            left set size
        m : int
            right set size
        preferences : dict
            **OPTIONAL**
            dictionary of preference ranks
                keys are ints
                vals are lists of ints
            example, for K_{2,2}:
                {
                    0 : [2, 3],
                    1 : [3, 2],
                    2 : [0, 1],
                    3 : [1, 0]
                }
                indicating 1 prefers 3 over 2, etc.
        """
        self.preferences = preferences
        self.G = nx.complete_bipartite_graph(n, m)
        self.left, self.right = nx.bipartite.sets(self.G)

    def max_weight_matching(self):
        """
        Uses NetworkX to return a matching that maximizes edge weight.
        """
        return nx.bipartite.maximum_matching(self.G)

    def is_stable_matching(self, matching = None):
        """
        Checks if the provided matching is stable.

        Parameters
        ----------
        matching : dict
            keys and vals are both endpoints. if your graph is undirected,
        """
        if not self.preferences:
            raise ValueError("No preferences found.")

        for l in list(matching.keys())[:int(len(matching)/2)]:
            r = matching[l]
            if r != self.preferences[l][0] and l != self.preferences[r][0]:
                return False
        return True

    def score_preference_rank(self, preferences = None):
        """
        Re-weights edges according to a preference rank dictionary. We assume
        each vertex/node "assigns" n-i points to the ith vertex in its
        preference list. The weight of an edge/pair is the sum of the points
        assigned by the endpoints.

        Parameters
        ----------
        preferences : dict
            **overwrites preferences attribute if not None**
            dictionary of preference ranks
                keys are ints
                vals are lists of ints
            example, for K_{2,2}:
                {
                    0 : [2, 3],
                    1 : [3, 2],
                    2 : [0, 1],
                    3 : [1, 0]
                }
                indicating 1 prefers 3 over 2, etc.

        Notes
        -----
        Inspired by Problem 3.2.10 in [1]

        References
        ----------
        [1] West, Douglas Brent. “Matchings and Factors.” In Introduction to
        Graph Theory, 135-135. United States: Pearson, 2018.
        """
        if not self.preferences:
            if not preferences:
                raise ValueError("Need to provide preferences.")
            else:
                self.preferences = preferences
        else:
            if not preferences:
                pass
            else:
                self.preferences = preferences

        for e in self.G.edges():
            l_pref = preferences[e[0]] # preference rank for left node
            r_pref = preferences[e[1]] # preference rank for right node

            self.G[e[0]][e[1]]['weight'] = len(l_pref)-(l_pref.index(e[1])+1) \
                                        + len(r_pref)-(r_pref.index(e[0])+1)
        return None
