import sys
# sys.stdin = open("bookshelf.in")
input = sys.stdin.readline

n, l = map(int, input().split())
shelves = [tuple(map(int, input().split())) for _ in range(n)]
# print(shelves)

# dp[i] = heights after book (i + 1)
# ex. dp[0] = init value, dp[1] = height of book 0
dp = [float('inf') for _ in range(n + 1)]
dp[0] = 0
for i in range(n):
    curWidth = 0
    curHeight = 0
    # read books i to j
    for j in range(i, n):
        curWidth += shelves[j][1]
        curHeight = max(curHeight, shelves[j][0])
        if curWidth > l:
            break
        # go from book [i, j] (both inclusive)
        # ex. i = 0 and j = 0, dp[1] = after reading book 0
        # i = 0, j = 1 (read books 0 and 1), use dp[2]
        dp[j + 1] = min(dp[j + 1], dp[i] + curHeight)
# print(dp)
print(dp[n])


'''
brute force, fill shelves as you go
nvm... seems that decisions impact things later on (want to group tall shelves)

dp(i) represents the minimum total height for the first i books
TC: O(n ** 2)
'''
