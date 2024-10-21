#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations
minOperations2 = __import__('0-minoperations2').minOperations2

# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 9000
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 9000
# print("Min # of operations to reach {} char: {}".format(n, minOperations2(n)))

# n = 9
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


# print(int(5.0) == 5)

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations2(n)))
n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations2(n)))
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations2(n)))
n = 19170307
print("Min # of operations to reach {} char: {}".format(n, minOperations2(n)))
n = 2147483640
print("Min # of operations to reach {} char: {}".format(n, minOperations2(n)))