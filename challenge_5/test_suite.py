# -*- coding: utf-8 -*-
import unittest
from challenge_5 import process_list
from sorting_algos import insertion_sort, mergesort

"""Testing the solution to data challenge 5.

Here, I make use of unittest to check the functionality of my solution to data
challenge 5. A global variable (S_M) controls which sorting algorithm is tested;
setting S_M to "None" results in Python's internal timsort implementation being
used.

"""

__author__ = "Daniel Hannah"
__email__ = "dan@danhannah.site"

S_M = None  # Global variable for sorting method to use in testing.

class SorterTestCase(unittest.TestCase):
    """Testing the list sorter."""

    def test_empty_list(self):
        """Checks that empty lists are handled correctly."""
        to_sort = []
        correctly_sorted = []
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_list_no_int(self):
        """Checks that a list with no integers is handled correctly."""
        to_sort = ["abc", "dog", "cat", "frog", "zzz", "telephone"]
        correctly_sorted = sorted(to_sort)
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_list_no_str(self):
        """Checks that a list with no strings is handled correctly."""
        to_sort = ["123", "555", "212", "313", "111", "99"]
        correctly_sorted = ["99", "111", "123", "212", "313", "555"]
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_mixed_list_alphanum(self):
        """Checks that a list containing ints & strings is handled correctly."""
        to_sort = ["dog", "20", "bird", "cat", "431", "12", "ice", "9"]
        correctly_sorted = ["bird", "9", "cat", "dog", "12", "20", "ice", "431"]
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_non_alphanum_only(self):
        """Checks for correct handling of only non-alphanumeric characters."""
        to_sort = ["@!#$", "^^^^", "?!@?@#*@#$"]
        correctly_sorted = []
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_mixed_all(self):
        """Checks correct handling of string + int + non-alphanumeric chars."""
        to_sort = ["20", "cat", "bi?rd", "12", "do@g"]
        correctly_sorted = ["12", "bird", "cat", "20", "dog"]
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_duplicate_words(self):
        """Tests if duplicated words are properly handled."""
        to_sort = ["20", "cat", "bi?rd", "12", "do@g", "dog", "cat"]
        correctly_sorted = ["12", "bird", "cat", "20", "cat", "dog", "dog"]
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

    def test_duplicate_numbers(self):
        """Tests if duplicated numbers are properly handled."""
        to_sort = ["20", "20", "1", "1", "cat", "bi?rd", "12", "for#^get"]
        correctly_sorted = ["1", "1", "12", "20", "bird", "cat", "20", "forget"]
        self.assertEqual(process_list(to_sort, S_M), correctly_sorted)

if __name__ == "__main__":
    unittest.main()

