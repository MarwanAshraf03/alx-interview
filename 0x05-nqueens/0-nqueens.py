#!/usr/bin/env python3
"""nqueens solution module"""
from typing import Mapping


def possible_sols(n:int, pos: tuple, SolMap: Mapping) -> Mapping:
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

def possible(pos: tuple, SolMap: Mapping):
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
    # for col in range(n):
    #     if (-1, col)in solList:
    #         continue
    #     if (row, col) not in solList:
    #         return (row, col)
    # return None


solListt = []


def backTrack(row: int, n: int, SolMap: Mapping, sol: list):
    if row == n:
        print(100 * '!')
        solListt.append(sol.copy())
        print(solListt)
        sol.clear()
        # SolMap = {}
        # print(sol)
        # print(SolMap)
        return
    print("entered")
    print(f"{50 * '-'}row = {row}{50 * '-'}")
    # if len(solListt) > 0:
    #     solListt.pop()
    for col in range(n):

        # if len(solListt) == n-1 and row == 0:
        #     print(100 * "h")
        #     solListt.clear()
        if row == 0:
            print(100 * "X")
            SolMap = {}
        if len(sol) == n-1 and row == 0:
            print(100 * "h")
            sol.clear()
        print(f"{50 * '+'} iteration: {col} in row = {row} {50 * '+'}")
        pos = (row, col)
        if str((row, col-1)) in SolMap.keys():
            keysList = list(SolMap.keys())
            index = keysList.index(str((row, col-1)))
            for hk in range(index, len(keysList)):
                del SolMap[keysList[hk]]
        if (row, col-1) in sol:
            sol = sol[0:sol.index((row, col-1))]
            # sol.remove((row, col-1))
        print(f"before validation pos = {pos}")
        print(f"sol = {sol}")
        if possible(pos, SolMap):
            print(f"after validation pos = {pos}")
            SolMap = possible_sols(n, pos, SolMap)
            sol.append(pos)
            print(f"the str(row, col-1) = {(row, col-1)} while the sol = {sol} and the condition is {(row, col-1) in sol}")
            if (row, col-1) in sol:
                sol.remove((row, col-1))
                print(f"removed = {(row, col-1)}")
            print(f"the str(row, col-1) = {(row, col-1)} while the sol = {sol} and the condition is {(row, col-1) in sol}")
            # solListt.append(pos)
            # print(f"the str(row, col-1) = {(row, col-1)} while the solListt = {solListt} and the condition is {(row, col-1) in solListt}")
            # if (row, col-1) in solListt:
            #     solListt.remove((row, col-1))
            #     print(f"popped = {(row, col-1)}")
            # solListt.append(pos)
            # print(f"the str(row, col-1) = {(row, col-1)} while the solListt = {solListt} and the condition is {(row, col-1) in solListt}")
            backTrack(row + 1, n, SolMap, sol)
        else:
            # print(solListt)
            print(SolMap)
            li = list(SolMap.keys()).copy()
            for i in li:
                if f"({row}," in i:
                    del SolMap[i]
                    # sol.remove(tuple(i))
            # if len(solListt) > 0:
            #     solListt.pop()
            continue
    # return sol
        # if col == n-1:
        # if len(solListt) == n:
        #     print(f"{50 * '*'}solListt = {solListt}{50 * '*'}")
        #     # del SolMap[str(pos)]
        #     return
        #     # break

if __name__ == "__main__":
    print("start")
    backTrack(0, 6, {}, [])
    # print(f"solListt = {solListt}")
    print("solListt = \n")
    for s in solListt:
        print(s)