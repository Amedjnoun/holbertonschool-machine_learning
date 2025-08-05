#!/usr/bin/env python3
"""
Module that contains matrix_transpose function
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix
    
    Args:
        matrix: A 2D matrix
    
    Returns:
        A new transposed matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed
