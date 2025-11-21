import sys
# sys.stdin = open("umbrella.in")
input = sys.stdin.readline

n, m = map(int, input().split())
# print(n, m)
cows = sorted([int(input()) for _ in range(n)])
# print(cows)
umbrellas = [int(input()) for _ in range(m)]
sf = [float('inf')]
for i in range(m - 1, -1, -1):
    sf.append(min(sf[-1], umbrellas[i]))
sf = sf[::-1]
sf.pop()
# print(len(sf))
# print(sf)
# print(umbrellas)

# 0 cows to n cows covered
dp = [float('inf')] * (n + 1)
dp[0] = 0

# start cow
for i in range(n):
    # end cow
    for j in range(i, n):
        umbrella_size = (cows[j] - cows[i]) + 1
        cost = sf[umbrella_size - 1]
        dp[j + 1] = min(dp[j + 1], dp[i] + cost)
# print(dp)
print(dp[n])

'''
hmm! up to 5,000 cows, up to 100,000 umbrella sizes
n*m = 500 million, too slow
but wait, 5,000 * 5,000 / 2 = 12.5 million might be fast enough
do I try it anyway? sure, why not

memory-wise rolling dp will be needed (5k by 5k array is too expensive)

try going from 0 cows to n cows, 0 to n - 1, ... 0 to 1
          then 1 cow to n cows, 1 to n - 1, ... 

ok, so it looks like they're not in order... I'll have to find the minimum cost for each then
can that be done quickly? suffix minimum?
'''
