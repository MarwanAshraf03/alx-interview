#!/usr/bin/python3
"""nqueens solution module"""
import sys

def possible_sols(n, pos, SolMap):
    """adds the positions that are filled by the pos in the solMap"""
    print(f"\n=== possible_sols ===")
    print(f"Adding attack positions for pos: {pos}")
    
    SolMap[str(pos)] = []
    SolMap[str(pos)].append((pos[0], -1))  # row blocking
    SolMap[str(pos)].append((-1, pos[1]))  # column blocking
    
    for k in range(1, n):
        if pos[0] + k < n and pos[1] + k < n:
            SolMap[str(pos)].append((pos[0] + k, pos[1] + k))
        if pos[0] - k >= 0 and pos[1] - k >= 0:
            SolMap[str(pos)].append((pos[0] - k, pos[1] - k))
        if pos[0] + k < n and pos[1] - k >= 0:
            SolMap[str(pos)].append((pos[0] + k, pos[1] - k))
        if pos[0] - k >= 0 and pos[1] + k < n:
            SolMap[str(pos)].append((pos[0] - k, pos[1] + k))
    
    print(f"Updated SolMap for pos {pos}: {SolMap}")
    return SolMap

def possible(pos, SolMap):
    """returns the possible position in the row"""
    solList = [i for sublist in SolMap.values() for i in sublist]
    
    print(f"\n=== possible ===")
    print(f"Checking if position {pos} is possible")
    print(f"Current attack positions in SolMap: {solList}")
    
    if (pos[0], -1) in solList or (-1, pos[1]) in solList or pos in solList:
        print(f"Position {pos} is not possible")
        return False
    
    print(f"Position {pos} is possible")
    return True

solListt = []

def backTrack(row, n, SolMap, sol):
    """uses backtracking to find best solutions"""
    if row == n:
        print(f"\n=== Solution Found ===")
        print(f"Appending solution: {sol}")
        solListt.append(sol.copy())
        # sol.clear()
        return
    
    for col in range(n):
        if row == 0:
            SolMap = {}
            print(f"\nCleared SolMap for new initial row: {row}")
        
        if len(sol) == n - 1 and row == 0:
            sol.clear()
            print("\nCleared solution list for new attempt")
        
        pos = (row, col)
        print(f"\nAttempting position {pos} in row {row}")
        
        # Clean up previous row's column positions in SolMap
        if str((row, col-1)) in SolMap:
            keysList = list(SolMap.keys())
            index = keysList.index(str((row, col-1)))
            for hk in range(index, len(keysList)):
                del SolMap[keysList[hk]]
            print(f"Cleared columns from previous row: {SolMap}")
        
        if (row, col - 1) in sol:
            sol = sol[0:sol.index((row, col - 1))]
            print(f"Truncated solution list to: {sol}")
        
        if possible(pos, SolMap):
            SolMap = possible_sols(n, pos, SolMap)
            sol.append(pos)
            print(f"Added position {pos} to solution: {sol}")
            backTrack(row + 1, n, SolMap, sol)
        else:
            print(f"Skipping position {pos} as it is under attack")
            # Remove positions from SolMap related to the current row
            li = list(SolMap.keys()).copy()
            for i in li:
                if f"({row}," in i:
                    del SolMap[i]
            print(f"Updated SolMap after skip: {SolMap}")
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
    
    print("Starting N-Queens Solution")
    backTrack(0, n, {}, [])
    print("\nAll solutions:")
    for s in solListt:
        print(s)
