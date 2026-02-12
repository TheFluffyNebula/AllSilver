# I got to the right strategy by myself! hashing & rewind
# spent ~2h, ended up using AI for this one :/
# deepseek is insane for finding the -m - 1 * pow_m line
import sys
sys.stdin = open("censor.in")
sys.stdout = open("censor.out", 'w')
input = sys.stdin.readline

s = input().strip()
t = input().strip()
# print(s, t)

n = len(s)
m = len(t)

r = 31
MOD = 10 ** 9 + 7

# shave off the log factor
pow_m = pow(r, m, MOD)

def computeHash(strToHash):
    ret = 0
    for c in strToHash:
        ret = (ret * r + ord(c) - ord('a') + 1) % MOD
    return ret
tHash = computeHash(t)

curHash = 0
# use stack to store (character, hash)
stack = []

for i in range(n):
    curHash = (curHash * r + ord(s[i]) - ord('a') + 1) % MOD
    stack.append((s[i], curHash))
    
    if len(stack) >= m:
        if len(stack) == m:
            lastHash = stack[-1][1]
        else:
            lastHash = (stack[-1][1] - stack[-m - 1][1] * pow_m) % MOD
    
        if lastHash == tHash:
            for _ in range(m):
                stack.pop()
            if stack:
                curHash = stack[-1][1]
            else:
                curHash = 0

print(''.join(ch for ch, _ in stack))
