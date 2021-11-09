import requests


def get_oeis_entry(int_seq):
    """
    Employs HTTP requests to grab relevant entries from the On-Line Encyclopedia
    of Integer Sequences.

    Parameters
    ----------
    int_seq : list[int]
        the sequence of integers you want to query
    """
    int_seq = ",".join([str(i) for i in int_seq])
    url = "https://oeis.org/search?fmt=json&q="+int_seq
    return requests.get(url).json()["results"]
