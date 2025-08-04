#!/usr/bin/env python3
"""
Module that contains add_arrays function
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise
    
    Args:
        arr1: First array
        arr2: Second array
    
    Returns:
        A new list with element-wise sum, or None if shapes don't match
    """
    if len(arr1) != len(arr2):
        return None
    
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    
    return result
