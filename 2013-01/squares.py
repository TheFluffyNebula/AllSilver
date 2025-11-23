import sys
sys.stdin = open("squares.in")
sys.stdout = open("squares.out", 'w')
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
squares = [tuple(map(int, input().split())) for _ in range(n)]
squares.sort()
# print(squares)

ans = 0
found = False
# stand-in for BST
window = deque()
for R in range(n):
    window.append(squares[R])
    while window[-1][0] - window[0][0] >= k:
        window.popleft()
    # print(window)
    for i in range(len(window) - 1):
        if abs(window[i][1] - window[-1][1]) < k:
            if found:
                print(-1)
                exit()
            found = True
            ans = (k - abs(window[i][0] - window[-1][0])) * (k - abs(window[i][1] - window[-1][1]))

print(ans) if found else print(0)

'''
probably some sorting for more efficient comparisons
by x, then by y
for each square maintain all points within k units horizontally
ex. k = 2 --> squares within 1 away qualify
    k = 4 --> squares within 3 away
for all of these squares, for each new square that enters the window, 
need to find if there are any that are less than k away vertically
'''
