import sys
# sys.stdin = open("baleshare.in")
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
# print(a)

# num_bales, barn_2_sum, barn_3_sum
# memory-efficient version
dp = [[[False for _ in range(800)] for _ in range(800)] for _ in range(2)]
dp[0][0][0] = True
tot = 0
for i in range(n):
    tot += a[i]
    for j in range(700):
        for k in range(700):
            if dp[i % 2][j][k]:
                # put in barn 1, barn 2, or barn 3
                dp[(i + 1) % 2][j][k] = True
                dp[(i + 1) % 2][j + a[i]][k] = True
                dp[(i + 1) % 2][j][k + a[i]] = True
ans = 700
for j in range(700):
    for k in range(700):
        if dp[n%2][j][k]:
            difference = max(j, k, tot - j - k)
            ans = min(ans, difference)
print(ans)

'''
--sol peek--
I knew it, dp ._.
Let good[n][B_2][B_3] be "true" if one can reach a state using only bales 1..n in which B_2 and B_3 
denote the total amount of hay in barns 2 and 3 (just as in the problem statement).

wow, the code for it is so elegant
'''
