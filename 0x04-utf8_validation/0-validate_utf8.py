#!/usr/bin/python3
""" utf validation module """


def validUTF8(data):
    """ utf 8 validation function """
    num_bytes = 0
    masks = [
        0b10000000,
        0b11000000,
        0b11100000,
        0b11110000,
        0b11111000
    ]
    for byte in data:
        if byte > 255:
            return False
        byte = byte & 0xFF
        if num_bytes == 0:
            if (byte & masks[1]) == masks[0]:
                continue
            elif (byte & masks[2]) == masks[1]:
                num_bytes = 1
            elif (byte & masks[3]) == masks[2]:
                num_bytes = 2
            elif (byte & masks[4]) == masks[3]:
                num_bytes = 3
            else:
                return False
        else:
            if (byte & masks[1]) != masks[0]:
                return False
            num_bytes -= 1
    return num_bytes == 0
