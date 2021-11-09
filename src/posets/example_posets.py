from itertools import chain, combinations

class ExamplePosets():
    """
    """
    def __init__(self):
        return None

    def boolean_lattice(self, n):
        """
        Generates a coverage_list for the Boolean lattice B_n.

        Parameters
        ----------
        n : `int`
            value of n specifying B_n

        Returns
        -------
        coverage_list : `list`
            list of coverage statements defining the poset

        Example Usage
        -------------
        >>> coverage = example_posets.ExamplePosets().boolean_lattice(4)
        {'_': ['1', '2', '3', '4'], '1': ['12', '13', '14'],
        '2': ['12', '23', '24'], '3': ['13', '23', '34'],
        '4': ['14', '24', '34'], '12': ['123', '124'], '13': ['123', '134'],
        '14': ['124', '134'], '23': ['123', '234'], '24': ['124', '234'],
        '34': ['134', '234'], '123': ['1234'], '124': ['1234'], '134': ['1234'],
        '234': ['1234']}
        """
        bracket_n = [str(i) for i in range(1, n+1)]
        sublists = list(chain(
            *(combinations(bracket_n, i) for i in range(len(bracket_n) + 1))))
        coverage_list = []
        for sublist1 in sublists:
            for sublist2 in sublists:
                if set(sublist1).issubset(set(sublist2)) \
                        and sublist1 != sublist2 \
                        and len(sublist1) == len(sublist2) - 1:
                    sublist1_str = "".join(sublist1)
                    if sublist1_str == "":
                        sublist1_str = "_"
                    sublist2_str = "".join(sublist2)
                    if sublist2_str == "":
                        sublist2_str = "_"
                    coverage_list.append(sublist1_str + "<" + sublist2_str)
        return coverage_list

    def finite_chain(self, length):
        """
        Generates a finite chain of specified length.

        Parameters
        ----------
        length : `int`
            number of items you want in the chain

        Returns
        -------
        ~ output ~ : `list`
            list of coverage statements defining the poset
        """
        return [str(i) + "<" + str(i+1) for i in range(1, length)]
