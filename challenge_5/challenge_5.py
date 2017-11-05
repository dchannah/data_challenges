# -*- coding: utf-8 -*-
import argparse
import re
from sorting_algos import insertion_sort, mergesort

"""Insight Data Science: Challenge 5

This program takes a list of mixed-content strings as input and spits out a
sorted list. The list will be sorted in the following way:

    20 cat bi?rd 12 do@g >> 12 bird cat 20 dog

Non-alphanumeric characters will be removed.

"""

__author__ = "Daniel Hannah"
__email__ = "dan@danhannah.site"


def read_cmd_line():
    """Reads command line arguments from input.
    
    :return: Filenames for input and output files and sorting algoritm.  
    """
    # Create an ArgumentParser
    psr = argparse.ArgumentParser(description="Insight Data Challenge 5")
    psr.add_argument('i', type=str, help="Path to input file.")
    psr.add_argument('o', type=str, help="Path to output file.")
    psr.add_argument('-a', type=str, default=None, help="Sorting algo to use.")

    # Get the sorting algorithm from the command line argument.
    sorting_dict = {"insertion_sort": insertion_sort,
                    "mergesort": mergesort,
                    None: None}

    # Read the command line arguments, give back separate in and out files.
    args = psr.parse_args()
    return args.i, args.o, sorting_dict[args.a]


def read_infile(input_file):
    """read_infile

    Converts an input file with space-separated strings to a list of strings.

    :param input_file: Path to input file.
    :return: A list of strings.
    """
    with open(input_file, 'r') as f:
        return f.readline().rstrip().split(" ")


def classify_list(list_of_strings):
    """classify_list

    Figures out if each string is digits, characters, or garbage.
    
    :param list_of_strings: A (cleaned) list of strings.
    :return: (list of int indices, list of str indices)
    """
    # Create lists to hold classification results.
    int_indices = []
    str_indices = []

    # Loop through and store type of every index.
    for idx, val in enumerate(list_of_strings):

        if val[0].isdigit():
            int_indices.append(idx)
        else:
            str_indices.append(idx)

    return int_indices, str_indices


def clean_word(string):
    """clean_word

    Removes non-digit, non-letter characters from a word.

    :param string: A string containing words, characters, and other stuff.
    :return: A cleaned string containing only digits or letters.
    """
    cleaner = re.compile(r'[^a-zA-Z0-9]')
    return cleaner.sub('', string)


def clean_list(list_of_strings):
    """clean_list

    Removes non-digit, non-letter characters from every item in the list.

    :param list_of_strings: List of strings.
    :return: A cleaned list of strings.

    """
    return list(filter(None, [clean_word(word) for word in list_of_strings]))


def sort_list(lst, method=None):
    """sort_list

    Sorts a list of integers or strings (should work for both).

    :param lst: A list of int or str dtypes.
    :param method: Sorting method, None means use Python's built-in.
    :return: None (lists are sorted in place)

    """
    if method is None:
        return sorted(lst)
    else:
        return method(lst)


def update_positions(orig_list, new_vals, positions):
    """update_positions

    Updates 

    :param orig_list: Original (cleaned) list.
    :param new_vals: New values (i.e. the sorting results)
    :param positions: Positions in the original list of the new values.
    :return: None (in place update of orig_list)

    """
    for idx, val in enumerate(new_vals):
        idx_to_update = positions[idx]
        orig_list[idx_to_update] = str(val)  # Convert back to string for easy testing.

    return


def process_list(lst, s_m=None):
    """process_list
    
    Cleans a list of all non-alphanumeric characters, then sorts the integers
    and the strings in place; ints are sorted back into int indices and strings
    are sorted back into string indices.

    :param lst: List object
    :param s_m: A sorting method (default None --> use Python's timsort)
    :return: A cleaned and sorted list.

    """
    # First, if the list is empty, just hand back an empty list.
    if len(lst) == 0:
        return []

    c_l = clean_list(lst)  # Remove all non-alphanumeric characters from list.
    int_loc, str_loc = classify_list(c_l)  # Get int and str indices.
    
    # Sort the ints and strings, respectively.
    sorted_ints = sort_list([int(c_l[idx]) for idx in int_loc], method=s_m)
    sorted_strs = sort_list([c_l[idx] for idx in str_loc], method=s_m)

    # Replace the int and str indices with the sorted versions.
    update_positions(c_l, sorted_ints, int_loc)
    update_positions(c_l, sorted_strs, str_loc)

    return c_l  # Return c_l because the update was done in place.


def main():
    """main method"""
    # Process the command line arguments and turn input into list of strings.
    infile, outfile, sorting_method = read_cmd_line()
    list_of_strings = read_infile(infile)

    # Clean and sort the list appropriately.
    processed_list = process_list(list_of_strings, sorting_method)

    # Write the cleaned and sorted list to the specific output file.
    with open(outfile, 'w') as o_f:
        o_f.write(" ".join(processed_list))


if __name__ == "__main__":
    main()

