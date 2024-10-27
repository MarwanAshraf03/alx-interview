#!/usr/bin/python3
"""
Main file for testing
"""
import time
minOperations = __import__('0-minoperations').minOperations

start = time.time()
print(minOperations(19170307))
end = time.time()
print(end - start)