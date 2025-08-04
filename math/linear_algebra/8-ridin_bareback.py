#!/usr/bin/env python3
"""
Module that contains mat_mul function
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication
    
    Args:
        mat1: First 2D matrix
        mat2: Second 2D matrix
    
    Returns:
        A new matrix representing the product, or None if incompatible
    """
    if len(mat1[0]) != len(mat2):
        return None
    
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum_product = 0
            for k in range(len(mat2)):
                sum_product += mat1[i][k] * mat2[k][j]
            row.append(sum_product)
        result.append(row)
    
    return result
