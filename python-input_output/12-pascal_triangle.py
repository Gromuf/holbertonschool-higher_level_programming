#!/usr/bin/python3
"""
This module defines the function pascal_triangle(n) that returns
a list of lists of integers representing Pascal’s triangle of n.

Pascal's Triangle is a triangular array of binomial coefficients.
Each element is the sum of the two directly above it.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        List[List[int]]: A list of lists of integers representing
        Pascal's triangle up to the nth row. Returns an empty list
        if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
