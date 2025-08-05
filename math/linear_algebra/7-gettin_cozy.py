#!/usr/bin/env python3
"""
Module that contains cat_matrices2D function
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis

    Args:
        mat1: First 2D matrix
        mat2: Second 2D matrix
        axis: Axis along which to concatenate (0 for rows, 1 for columns)

    Returns:
        A new concatenated matrix, or None if incompatible
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = []
        for i in range(len(mat1)):
            new_row = mat1[i][:] + mat2[i][:]
            result.append(new_row)
        return result

    return None
