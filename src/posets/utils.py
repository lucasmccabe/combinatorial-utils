import itertools

def parse_coverage_list(coverage_list):
    """
    Given a coverage_list (structured as a list of coverage statements (which
    are strings) that define the poset, parses them into a dictionary.

    Parameters
    ----------
    coverage_list : `list`
        list of coverage statements defining a poset, e.g.:
            ["_<1",
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

    Returns
    -------
    coverage_dict : `dict`
        keys are items in the poset, other than the maximal element
        values are items in the poset that cover their respective key

    Example Usage
    -------------
    >>> coverage_list = [
    ...    "_<1",
    ...    "_<2",
    ...    "_<3",
    ...    "1<12",
    ...    "1<13",
    ...    "2<12",
    ...    "2<23",
    ...    "3<13",
    ...    "3<23",
    ...    "13<123",
    ...    "12<123",
    ...    "23<123"]
    >>> parse_coverage_list(coverage_list)
    {'_': ['1', '2', '3'],
     '1': ['12', '13'],
     '2': ['12', '23'],
     '3': ['13', '23'],
     '13': ['123'],
     '12': ['123'],
     '23': ['123']}
    """
    coverage_dict = {}
    if "<" not in coverage_list[0]:
        coverage_dict[coverage_list[0]] = []
    for i in [j.split("<") for j in coverage_list]:
        for j in range(len(i)-1):
            if i[j] not in coverage_dict.keys():
                coverage_dict[i[j]] = []
            coverage_dict[i[j]].append(i[j+1])
    return coverage_dict
