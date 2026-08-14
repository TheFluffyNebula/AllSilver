import sys
sys.stdin = open("cownomics.in")
sys.stdout = open("cownomics.out", 'w')

lookup = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
n, m = map(int, input().split())
spotty = [list(map(lambda x: lookup[x], input().strip())) for _ in range(n)]
plain = [list(map(lambda x: lookup[x], input().strip())) for _ in range(n)]
# print(spotty, plain)

def valid(a, b, c):
    spottyCount = [0] * 64
    plainCount = [0] * 64
    for i in range(n):
        x = spotty[i][a] * 16 + 4 * spotty[i][b] + spotty[i][c]
        spottyCount[x] += 1
    for i in range(n):
        x = plain[i][a] * 16 + 4 * plain[i][b] + plain[i][c]
        plainCount[x] += 1
    for i in range(64):
        if spottyCount[i] and plainCount[i]:
            return 0
    return 1

ans = 0
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            ans += valid(i, j, k)
print(ans)
'''
goal: find subsequences of 3 that appear in the top n but not the bottom n
50C3 = 20000
20k * 1000 = 20m rows to check
possible.
'''
