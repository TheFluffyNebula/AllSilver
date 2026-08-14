import sys
sys.stdin = open("where.in")
sys.stdout = open("where.out", 'w')

n = int(input())
board = [input().strip() for _ in range(n)]
# print(*board, sep='\n')

def checkCont(color, sR, eR, sC, eC, stackR, stackC):
    cCount = 0
    for r in range(sR, eR + 1):
        for c in range(sC, eC + 1):
            if board[r][c] == color:
                cCount += 1
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[stackR][stackC] = True
    compCount = 1
    stack = [(stackR, stackC)]
    while stack:
        uR, uC = stack.pop()
        for dR, dC in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            vR, vC = uR + dR, uC + dC
            if not (sR <= vR <= eR and sC <= vC <= eC):
                continue
            if board[vR][vC] != color:
                continue
            if not visited[vR][vC]:
                visited[vR][vC] = True
                stack.append((vR, vC))
                compCount += 1
    if compCount == cCount:
        return 1
    return 0

def check(sR, eR, sC, eC):
    colors = []
    start = []
    for r in range(sR, eR + 1):
        for c in range(sC, eC + 1):
            if board[r][c] not in colors:
                colors.append(board[r][c])
                start.append((r, c))
                if len(colors) > 2:
                    return
    if len(colors) < 2:
        return
    numContiguous = 0
    numContiguous += checkCont(colors[0], sR, eR, sC, eC, start[0][0], start[0][1])
    numContiguous += checkCont(colors[1], sR, eR, sC, eC, start[1][0], start[1][1])
    if numContiguous == 1:
        area = (eR - sR + 1) * (eC - sC + 1)
        PCL_unfiltered.append((area, sR, eR, sC, eC))

PCL_unfiltered = []
for startRow in range(n):
    # inclusive indices
    for endRow in range(startRow, n):
        for startCol in range(n):
            for endCol in range(startCol, n):
                # min viable is 3, ex. ABA
                if (endRow - startRow + 1) * (endCol - startCol + 1) < 3:
                    continue
                check(startRow, endRow, startCol, endCol)
# (area, sR, eR, sC, eC)
PCL_unfiltered.sort(reverse=True)
# print(PCL_unfiltered)
PCL_filtered = []
for area, sR, eR, sC, eC in PCL_unfiltered:
    valid = True
    for curArea, curSR, curER, curSC, curEC in PCL_filtered:        
        if (curSR <= sR <= eR <= curER) and (curSC <= sC <= eC <= curEC):
            valid = False
            break
    if valid:
        PCL_filtered.append((area, sR, eR, sC, eC))
# print(PCL_filtered)
print(len(PCL_filtered))

'''
start w/ finding largest PCLs, brute force every single possible rectangle
1st check: 2 colors
2nd check: 1 continuous, other color not continuous
finally, sort by area in reverse order, guarantees subset friendliness
keep those that are disjoint
output PCL count
'''
