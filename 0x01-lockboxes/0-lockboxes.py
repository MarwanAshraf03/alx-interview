#!/usr/bin/python3
"""Module"""


def canUnlockAll(boxes):
    """function"""
    ln = len(boxes) - 1
    summation = (ln/2) * (2 * 1 + (ln - 1) * 1)
    list_of_keys = boxes[0][:]
    if summation == sum(set(list_of_keys)):
        return True
    lcopy = list_of_keys.copy()
    for i in range(len(boxes)):
        for key in lcopy:
            if key > ln:
                continue
            list_of_keys.extend(boxes[key])
            if summation == sum(set(list_of_keys)):
                return True
            lcopy = set(list_of_keys.copy())
    return False
