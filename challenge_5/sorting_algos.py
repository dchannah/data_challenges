# -*- coding: utf-8 -*-

"""Sorting algorithms for data challenge 5

This is a collection of locally-implemented sorting methods to demonstrate the
impact of sorting algorithm efficiency on the overall time complexity of this
data challenge 5 solution.

"""

__author__ = "Daniel Hannah"
__email__ = "dan@danhannah.site"


def insertion_sort(lst):
    l_s = lst.copy()
    i = 1
    while i < len(l_s):
        j = i
        while j > 0 and l_s[j - 1] > l_s[j]:
            l_s[j], l_s[j - 1] = l_s[j - 1], l_s[j]
            j = j - 1
        i = i + 1
    return l_s


def mergesort(lst):
    result = []
    if len(lst) < 2:
        return lst
    mid = int(len(lst) / 2)
    y = mergesort(lst[:mid])
    z = mergesort(lst[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result
