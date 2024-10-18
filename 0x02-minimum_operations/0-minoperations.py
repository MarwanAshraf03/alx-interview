#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    """
    finds min number of operations to print H for n times
    using only two operations (Copy All and Paste)
    """
    l_of_p_nums = []
    for x in range(2, n):
        is_p = True
        for y in range(2, int(x / 2)+1):
            if (x / y) % 2 == 0:
                is_p = False
        if is_p:
            l_of_p_nums.append(x)
    if n in l_of_p_nums:
        return 0
    llll = []
    n1 = n
    while True:
        n2 = helper(n1, l_of_p_nums)
        llll.append(n2)
        n1 /= n2
        if llll[-1] == -1:
            break
    return sum(llll)+1


def helper(nn, lofp):
    """
    helper function to get the min prime number
    that nn is divisible by
    """
    if nn == 1:
        return -1
    for i in lofp:
        if (nn / i) == int(nn / i):
            return i
    return -1
