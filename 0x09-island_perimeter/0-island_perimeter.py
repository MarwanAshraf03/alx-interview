#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """
    A function that calculates
    the perimeter of an island (grid)
    a 2 * 2 matrix
    """
    perimeter = 0
    add = 0
    sumofsums = 0
    if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0]:
        return 4
    for i in grid:
        sumofsums += sum(i)
    if sumofsums == len(grid) * len(grid[0]):
        return sumofsums
    if len(grid) == 1:
        for j in range(len(grid[0])):
            add = grid[0][j]
            if add == 1:
                add *= 4
                try:
                    if grid[0][j-1] == 1:
                        if j != 0:
                            add -= 1
                    if grid[0][j+1] == 1:
                        add -= 1
                except IndexError:
                    pass
            perimeter += add
    else:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                add = grid[i][j]
                if add == 1:
                    add *= 4
                    try:
                        if grid[i][j-1] == 1:
                            add -= 1
                        if grid[i-1][j] == 1:
                            add -= 1
                        if grid[i][j+1] == 1:
                            add -= 1
                        if grid[i+1][j] == 1:
                            add -= 1
                    except IndexError:
                        pass
                perimeter += add
    return perimeter
