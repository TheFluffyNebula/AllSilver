import sys
sys.stdin = open("bgm.in")
sys.stdout = open("bgm.out", 'w')

'''
how many ways can we make at least one of the product quantities a multiple of 7?
I'm pretty sure 7^7 = 800k brute force works here
'''

letterToNum = {
    "B": 0, 
    "E": 1, 
    "S": 2,
    "I": 3,
    "G": 4,
    "O": 5,
    "M": 6
}

n = int(input())
# letter, mod 7-count
counts = [[0 for _ in range(7)] for _ in range(7)]
for i in range(n):
    letter, val = input().split()
    val = int(val)
    counts[letterToNum[letter]][val % 7] += 1

ans = 0
# use base 7
for i in range(7 ** 7):
    cur = 1
    x = i
    vals = []
    for i in range(7):
        idx = x % 7
        # ex. B = ones digit, i % 7 = 0 -> select counts[0][0]
        cur *= counts[i][idx]
        x //= 7
        vals.append(idx)
    if (vals[0] + 2 * vals[1] + 2 * vals[2] + vals[3]) * \
        (vals[4] + vals[5] + vals[1] + vals[2]) * \
        (vals[6] + 2 * vals[5]) % 7 == 0:
        ans += cur
print(ans)
