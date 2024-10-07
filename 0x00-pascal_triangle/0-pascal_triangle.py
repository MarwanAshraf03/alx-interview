#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """Pascal's Triangle Module"""

    if n <= 0:
        return ([])
    l_of_l = []
    for i in range(1, n+1):
        if i == 1:
            l_of_l.append([1])
            continue
        new_l = [1]
        nn = 0
        if i % 2 == 0:
            for j in range(1, int(len(l_of_l[i-2])/2+1)):
                new_l.append(l_of_l[i-2][nn] + l_of_l[i-2][j])
                nn = j
            new_l += list(reversed(new_l))[:]
        if i % 2 != 0:
            for j in range(1, int(len(l_of_l[i-2])/2+1)):
                new_l.append(l_of_l[i-2][nn] + l_of_l[i-2][j])
                nn = j
            new_l += list(reversed(new_l[:-1]))[:]
        l_of_l.append(new_l)
    return (l_of_l)
