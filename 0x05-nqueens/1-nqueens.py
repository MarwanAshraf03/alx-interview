#!/usr/bin/env python3
from typing import Mapping
n = 4
solutions = {}


def possible(pos: tuple, black_out_positions: list):
    """returns the possible position in the row"""
    print(f"pos = {pos}, black_out_positions = {black_out_positions}")
    if (pos[0], -1) in black_out_positions:
        return False
    if (-1, pos[1]) in black_out_positions:
        return False
    if pos in black_out_positions:
        return False
    return True

def add_black_out_positions(pos: tuple, black_out_positions: list):
    black_out_positions.append((pos[0], -1))
    black_out_positions.append((-1, pos[1]))
    for k in range(1, n):
        if pos[0]+k <= n and pos[1]+k <= n:
            black_out_positions.append((pos[0]+k, pos[1]+k))
        if pos[0]-k >= 0 and pos[1]-k >= 0:
            black_out_positions.append((pos[0]-k, pos[1]-k))
        if pos[0]+k <= n and pos[1]-k >= 0:
            black_out_positions.append((pos[0]+k, pos[1]-k))
        if pos[0]-k >= 0 and pos[1]+k <= n:
            black_out_positions.append((pos[0]-k, pos[1]+k))
    return black_out_positions


# for row in range(n):
#     for col in range(n):
#         pos = (row, col)
#         solutions[str(pos)] = {}
#         black_out_positions = add_black_out_positions(pos, black_out_positions)
#         for i in range(n):
#             new_pos = (row+1, i)
#             if possible(new_pos, black_out_positions):
#                 solutions[str(pos)][str(new_pos)] = {}
for col in range(n):
    black_out_positions = []
    pos = (0, col)
    print(f"pos = {pos}")
    solutions[str(pos)] = {}
    black_out_positions = add_black_out_positions(pos, black_out_positions)
    for i in range(n):
        new_pos = (1, i)
        if possible(new_pos, black_out_positions):
            solutions[str(pos)][str(new_pos)] = {}

def back_track():
    pass

print(solutions)