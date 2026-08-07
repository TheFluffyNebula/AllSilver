import sys
sys.stdin = open("cowcode.in")
sys.stdout = open("cowcode.out", 'w')

s, n = input().split()
n = int(n)
sLen = len(s)

if n <= sLen:
    print(s[n - 1])
    exit()

c = sLen
pows = [sLen]
while c <= n:
    c *= 2
    pows.append(c)
# print(pows)

for i in range(len(pows) - 2, -1, -1):
    if 2 * pows[i] >= n and n > pows[i]:
        secondIdx = n - pows[i]
        firstIdx = secondIdx - 1 # <-- the new n?
        if firstIdx == 0: firstIdx = pows[i]
        n = firstIdx
    if n <= sLen:
        print(s[n - 1])
        exit()
assert False

'''
pattern finding
classic archetype :) (saw it this year, 2025-2026)
'''
