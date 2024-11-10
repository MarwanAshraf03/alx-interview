#!/usr/bin/python3
"""nqueens solution module"""
import sys
# n = 4


def possible_sols(n, pos, SolMap):
    """adds the positions that are filled by the pos in the solMap"""
    SolMap[str(pos)] = []
    SolMap[str(pos)].append((pos[0], -1))
    SolMap[str(pos)].append((-1, pos[1]))
    # if (rT or rT2 or cT or cT2):
    #     return SolMap
    for k in range(1, n):
        if pos[0]+k <= n and pos[1]+k <= n:
            SolMap[str(pos)].append((pos[0]+k, pos[1]+k))
        if pos[0]-k >= 0 and pos[1]-k >= 0:
            SolMap[str(pos)].append((pos[0]-k, pos[1]-k))
        if pos[0]+k <= n and pos[1]-k >= 0:
            SolMap[str(pos)].append((pos[0]+k, pos[1]-k))
        if pos[0]-k >= 0 and pos[1]+k <= n:
            SolMap[str(pos)].append((pos[0]-k, pos[1]+k))
    return SolMap


def possible(pos, SolMap):
    """returns the possible position in the row"""
    solList = [i[:] for i in SolMap.values()]
    solList = [i for j in solList for i in j]
    if (pos[0], -1) in solList:
        return False
    if (-1, pos[1]) in solList:
        return False
    if pos in solList:
        return False
    return True


solListt = []


def backTrack(row, n, SolMap, sol):
    """uses backtracking to find best solutions"""
    if row == n:
        solListt.append(sol.copy())
        sol.clear()
        return
    for col in range(n):
        if row == 0:
            SolMap = {}
        if len(sol) == n-1 and row == 0:
            sol.clear()
        pos = (row, col)
        if str((row, col-1)) in SolMap.keys():
            keysList = list(SolMap.keys())
            index = keysList.index(str((row, col-1)))
            for hk in range(index, len(keysList)):
                del SolMap[keysList[hk]]
        if (row, col-1) in sol:
            sol = sol[0:sol.index((row, col-1))]
        if possible(pos, SolMap):
            SolMap = possible_sols(n, pos, SolMap)
            sol.append(pos)
            if (row, col-1) in sol:
                sol.remove((row, col-1))
            backTrack(row + 1, n, SolMap, sol)
        else:
            li = list(SolMap.keys()).copy()
            for i in li:
                if f"({row}," in i:
                    del SolMap[i]
            continue


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    backTrack(0, n, {}, [])
    for s in solListt:
        print(s)
