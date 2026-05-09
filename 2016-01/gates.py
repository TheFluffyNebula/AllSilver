# I don't think I'm counting the boxes the correct way here
import sys
sys.stdin = open("gates.in")
sys.stdout = open("gates.out", 'w')
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
s = input().strip()

directionMap = {
    "N": (0, 1), 
    "S": (0, -1), 
    "E": (1, 0), 
    "W": (-1, 0)
}

curX, curY = 0, 0
ans = 0
visited = defaultdict(int)
gates = defaultdict(int)
visited[(0, 0)] = True
for i in range(n):
    prev = (curX, curY)
    curX += directionMap[s[i]][0]
    curY += directionMap[s[i]][1]
    next = (curX, curY)
    if not visited[(curX, curY)]:
        visited[(curX, curY)] = True
    else:
        if not gates[(prev, next)]:
            gates[(prev, next)] = 1
            gates[(next, prev)] = 1
            ans += 1
print(ans)
'''
theory: ans = # boxes
whenever we visit a previously visited square, boxes += 1
last step: remove duplicates
hmm... alright, new plan
let everything be two steps
plan the borders
flood fill to find the number of boxes
'''