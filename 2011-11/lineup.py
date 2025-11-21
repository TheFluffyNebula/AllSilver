import sys
# sys.stdin = open("lineup.in")
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()
# print(cows)
uniqueBreeds = len(set([x[1] for x in cows]))
# print(uniqueBreeds)

L = 0
breeds = defaultdict(int)
curBreeds = 0
best = float('inf')
for R in range(n):
    breeds[cows[R][1]] += 1
    if breeds[cows[R][1]] == 1:
        curBreeds += 1
    
    while curBreeds == uniqueBreeds:
        # print(L, R)
        best = min(best, cows[R][0] - cows[L][0])
        breeds[cows[L][1]] -= 1
        if breeds[cows[L][1]] == 0:
            curBreeds -= 1
        L += 1
    # print(L, R)
print(best)

'''
2 Pointers/Sliding Window
'''
