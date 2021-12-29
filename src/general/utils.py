import requests


def get_oeis_entry(int_seq):
    """
    Employs HTTP requests to grab relevant entries from the On-Line Encyclopedia
    of Integer Sequences.

    Parameters
    ----------
    int_seq : list[int]
        the sequence of integers you want to query

    Example Usage
    -------------
    Retrieve the OEIS entry for a sequence beginning with {1, 2, 3}:

        >>> tusc.general.get_oeis_entry([1,2,3])
        [{'number': 45,
          'id': 'M0692 N0256',
          'data': '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,
            4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,
            832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,
            39088169,63245986,102334155',
          'name': 'Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and
            F(1) = 1.',
          'comment': ['D. E. Knuth writes: "Before Fibonacci wrote his work, the
            sequence F_{n} had already been discussed by Indian scholars, who
            had long been interested in rhythmic patterns that are formed from
            one-beat and two-beat notes. The number of such rhythms having n
            beats altogether is F_{n+1}; therefore both Gopāla (before 1135) and
            Hemachandra (c. 1150) mentioned the numbers 1, 2, 3, 5, 8, 13, 21,
        ...
    """
    int_seq = ",".join([str(i) for i in int_seq])
    url = "https://oeis.org/search?fmt=json&q="+int_seq
    return requests.get(url).json()["results"]
