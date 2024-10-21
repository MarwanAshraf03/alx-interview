#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    """
    finds min number of operations to print H for n times
    using only two operations (Copy All and Paste)
    """
    llll = []
    n1 = n
    while True:
        n2 = helper(n1)
        llll.append(n2)
        n1 /= n2
        if llll[-1] == -1:
            break
    return sum(llll)+1


def helper(nn):
    """
    helper function to get the min prime number
    that nn is divisible by
    """
    lofp = []
    if nn == 1:
        return -1
    if (nn/2) == int(nn/2):
        return 2
    for i in range(3, int(nn)+3, 2):
        is_p = True
        for j in range(2, int(i/2)+1):
            if (i / j) % 2 == 0:
                is_p = False
        if is_p:
            lofp.append(i)
            if (nn / i) == int(nn / i):
                return i
    if (nn in lofp):
        return nn
    return -1
