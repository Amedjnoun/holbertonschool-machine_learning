#!/usr/bin/env python3
"""
Module that contains matrix_shape function
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix

    Args:
        matrix: A matrix (nested list)

    Returns:
        A list of integers representing the shape
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) > 0:
            matrix = matrix[0]
        else:
            break
    return shape
