#!/usr/bin/python3
"""A module to rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """the function that performs an inplace 2d matrix rotation"""
    nrows = len(matrix)
    ncols = len(matrix[0])
    matrix2 = matrix[:]
    for i in range(nrows):
        app = []
        for j in range(ncols):
            app.append(matrix2[(nrows-1)-j][i])
        matrix[i] = app.copy()
