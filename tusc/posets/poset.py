import itertools
from .utils import *

class Poset():
    """
    Class for handling finite posets, representing them as dicts.

    Example Usage
    -------------
    Examples will use the following coverage_list (the Boolean lattice B_3):
        coverage = [
            "_<1",
            "_<2",
            "_<3",
            "1<12",
            "1<13",
            "2<12",
            "2<23",
            "3<13",
            "3<23",
            "13<123",
            "12<123",
            "23<123"]
    """
    def __init__(
            self,
            coverage_list = None,
            coverage_dict = None):
        """
        Constructor for the Poset class.

        Parameters
        ----------
        coverage_list : `list`
            list of coverage statements defining a poset
            *optional, but one of coverage_list or coverage_dict must be passed.
        coverage_dict : `dict`
            keys are items in the poset, other than the maximal element
            values are items in the poset that cover their respective key
            *optional, but one of coverage_list or coverage_dict must be passed.
        """
        if not coverage_dict and not coverage_list:
            raise ValueError("Must provide a coverage_dict or coverage_list.")
        elif not coverage_dict:
            self.coverage_dict = parse_coverage_list(coverage_list)
        else:
            self.coverage_dict = coverage_dict
        return None

    def get_zero(self):
        """
        Returns the \hat{0} of the poset, if it exists.

        Returns
        -------
        i : `str`
            \hat{0} of the poset

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.get_zero())
        _
        """
        for i in self.all_elements():
            temp = True
            for j in self.all_elements():
                if i == j:
                    continue
                if not self.is_lessthan(i, j):
                    temp = False
                    break
            if temp:
                break
        if temp:
            return i
        else:
            raise ValueError("No \hat{0} found.")

    def get_one(self):
        """
        Returns the \hat{1} of the poset, if it exists.

        Returns
        -------
        i : `str`
            \hat{1} of the poset

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.get_one())
        123
        """
        for i in self.all_elements():
            temp = True
            for j in self.all_elements():
                if i == j:
                    continue
                if not self.is_greaterthan(i, j):
                    temp = False
                    break
            if temp:
                break
        if temp:
            return i
        else:
            raise ValueError("No \hat{1} found.")

    def all_elements(self):
        """
        Returns all the elements of the poset.

        Returns
        -------
        ~ output ~ : `list`
            list of all the elements of the poset

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.all_elements())
        ['2', '123', '3', '12', '1', '_', '23', '13']
        """
        return list(
            set(
                list(itertools.chain(*list(self.coverage_dict.keys()))) \
                + list(itertools.chain(*list(self.coverage_dict.values())))))

    def is_lessthan(self, a, b):
        """
        Evaluates if a \leq b in the poset.

        Parameters
        ----------
        a : `str`
        b : `str`

        Returns
        -------
        ~ output ~ : `int`
            truth value 1 or 0

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.is_lessthan("_", "12"))
        1
        """
        if a not in self.coverage_dict.keys():
            return 0
        elif b in self.coverage_dict[a]:
            return 1
        else:
            return max(
                [self.is_lessthan(c, b) \
                for c in self.coverage_dict[a]])

    def is_greaterthan(self, a, b):
        """
        Evaluates if a \geq b in the poset.

        Parameters
        ----------
        a : `str`
        b : `str`

        Returns
        -------
        ~ output ~ : `int`
            truth value 1 or 0

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.is_greaterthan("_", "12"))
        0
        """
        return self.is_lessthan(b, a)

    def mobius(self, lower, upper):
        """
        Evaluates the Mobius function \mu(lower, upper) for the poset.

        Parameters
        ----------
        lower : `str`
        upper : `str`

        Returns
        -------
        ~ output ~ : `int`
            value of the Mobius function

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.mobius("_", "123"))
        -1
        """
        if lower == upper and lower in self.all_elements():
            return 1
        if not self.is_lessthan(lower, upper):
            raise ValueError("Lower is not less than upper.")
        s = 0
        for t in self.interval(lower, upper):
            s += self.mobius(lower, t)
        return -s

    def interval(self, lower, upper, with_upper = False):
        """
        Returns all items in the interval [lower, upper]

        Parameters
        ----------
        lower : `str`
        upper : `str`
        with_upper : `bool`
            describes whether to include upper in the returned list

        Returns
        -------
        ~ output ~ : `list`
            list of items in the interval

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.interval("_", "12"))
        ['_', '1', '2']
        """
        interval = [
            t for t \
            in self.all_elements() \
            if t == lower \
            or (self.is_lessthan(lower, t) \
                and self.is_lessthan(t, upper))]
        if with_upper:
            interval.append(upper)
        return interval


    def interval_len(self, lower, upper, l=0):
        """
        Returns the length of an interval.

        Parameters
        ----------
        lower : `str`
        upper : `str`

        Returns
        -------
        ~ output ~ : `int`
            length of the interval

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.interval_len("1", "123"))
        2
        """
        if lower == upper:
            return l
        if self.is_greaterthan(lower, upper):
            return self.interval_len(upper, lower, l)
        if not self.is_lessthan(lower, upper):
            raise ValueError("lower and upper are not comparable.")
        lens = [
            self.interval_len(i, upper, l+1) \
            for i in self.interval(lower, upper, with_upper = True) \
            if i != lower]
        return max(lens)

    def all_intervals(self):
        """
        Returns a list of all interval bounds (i, j), i \leq j, in the poset.

        Returns
        -------
        intervals : `list`
            list of tuples (i, j) representing interval bounds in the poset

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.all_intervals())
        [('_', '23'), ('_', '3'), ('_', '13'), ('_', '123'), ('_', '1'),
        ('_', '12'), ('_', '2'), ('23', '123'), ('3', '23'), ('3', '13'),
        ('3', '123'), ('13', '123'), ('1', '13'), ('1', '123'), ('1', '12'),
        ('12', '123'), ('2', '23'), ('2', '123'), ('2', '12')]
        """
        interval_bounds = [(i, j) \
            for i in self.all_elements() \
            for j in self.all_elements() \
            if self.is_lessthan(i, j)]
        return interval_bounds

    def is_semi_Eulerian(self):
        """
        Verifies if the poset is semi-Eulerian, assuming it is graded.

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.is_semi_Eulerian())
        True
        """
        for interval in self.all_intervals():
            if interval == (self.get_zero(), self.get_one()):
                continue
            if self.mobius(
                    interval[0],
                    interval[1]
                    ) != (-1)**self.interval_len(interval[0], interval[1]):
                return False
        return True

    def is_Eulerian(self):
        """
        Verifies if the poset is Eulerian, assuming it is graded.

        Example Usage
        -------------
        >>> p = poset.Poset(coverage)
        >>> print(p.is_Eulerian())
        True
        """
        for interval in self.all_intervals():
            if self.mobius(
                    interval[0],
                    interval[1]
                    ) != (-1)**self.interval_len(interval[0], interval[1]):
                return False
        return True
