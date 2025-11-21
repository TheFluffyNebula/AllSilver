import sys
sys.stdin = open("clumsy.in")
sys.stdout = open("clumsy.out", 'w')
input = sys.stdin.readline

s = input().strip()
n = len(s)

stack = 0
left = 0
maxLeft = n // 2
ans = 0
for i in range(n):
    if s[i] == '(':
        if left < maxLeft:
            left += 1
            stack += 1
        else:
            stack -= 1
            ans += 1
    else:
        # right parentheses
        if stack > 0:
            stack -= 1
        else:
            left += 1
            stack += 1
            ans += 1
print(ans)

'''
greedy -- just do it as needed
var keeping track of left-parens -- at this point all will need to be converted to right
'''
