import sys
sys.stdin = open("lazy.in")
sys.stdout = open("lazy.out", 'w')

beforeN, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(beforeN)]
# print(*b, sep='\n')

n = 2 * beforeN - 1
a = [[0 for i in range(n)] for j in range(n)]

startRow = 0
startCol = beforeN - 1
for i in range(beforeN):
    for j in range(beforeN):
        a[startRow + j][startCol + j] = b[i][j]
    startRow += 1
    startCol -= 1
# print(*a, sep='\n')

windowLen = 2 * k + 1
# answer is just everything, prevent error % return
if windowLen >= n:
    x = sum([sum(a[i]) for i in range(n)])
    print(x)
    exit()

# compute the first
topCorner = sum([sum(a[i][:windowLen]) for i in range(windowLen)])
ans = topCorner
# print(n, windowLen)

pf = []
for i in range(n):
    pf_row = [0]
    for j in range(n):
        pf_row.append(pf_row[-1] + a[i][j])
    pf.append(pf_row)
# print(pf)

# going by column then row so we can use row prefixes
for startC in range(n - windowLen):
    cur = topCorner
    ans = max(ans, cur)
    for startR in range(n - windowLen):
        # move the window down the column
        # pf[R + 1] - pf[L] where L & R are inclusive
        cur -= pf[startR][startC + windowLen - 1 + 1] - pf[startR][startC]
        cur += pf[startR + windowLen][startC + windowLen - 1 + 1] - pf[startR + windowLen][startC]
        # if startC == 0:
        #     print(pf[startR][startC + windowLen - 1 + 1] - pf[startR][startC], pf[startR + windowLen - 1][startC + windowLen - 1 + 1] - pf[startR + windowLen - 1][startC])
        #     print(cur)
        ans = max(ans, cur)
    # can't go over to another column
    if startC == n - windowLen - 1:
        break
    # move right a column (start at the top again)
    for i in range(windowLen):
        # goodbye startC, hello startC + windowLen
        topCorner -= a[i][startC]
        topCorner += a[i][startC + windowLen]

print(ans)
'''
I remember this being diagonal but never learned how...
time to try!

manual 2D prefix sums 💀
'''
