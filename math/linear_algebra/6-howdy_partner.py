#!/usr/bin/env python3
"""
Module that contains cat_arrays function
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays

    Args:
        arr1: First array
        arr2: Second array

    Returns:
        A new list containing concatenated arrays
    """
    result = []
    for element in arr1:
        result.append(element)
    for element in arr2:
        result.append(element)

    return result
