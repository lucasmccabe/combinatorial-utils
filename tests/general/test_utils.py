import unittest

from tusc import general

class TestUtils(unittest.TestCase):

    def test_get_oeis_entry_fibonacci(self):
        """
        Validates the OEIS entry returned by get_oeis_entry().
        """
        self.assertEqual(
            general.get_oeis_entry([1,2,3,5,8,13,21,34,55])[0]["id"],
            "M0692 N0256"
        )

    def test_get_oeis_entry_islist(self):
        """
        Tests that the get_oeis_entry() HTTP request returns a list.
        """
        self.assertTrue(
            type(general.get_oeis_entry([1,2,3,5,8,13,21,34,55])) == list
        )



if __name__ == "__main__":
    unittest.main()
