import sys
# sys.stdin = open("c.in")

# first attempt: brute force to try to secure TC 1-4/11
tc = int(input())

'''
observation: 
    when r_i == r_i-1, the bit that enters must be equal to the bit that leaves
    when they're different, enter bit != leaving bit
'''
def solve():
    n, k = map(int, input().split())
    # print(n, k)
    s = input().strip()
    if k == 1:
        print(s.count("1"), s.count("1"))
        return
    mn = 10 ** 7
    mx = 0
    for mask in range(2 ** k):
        binS = list(bin(mask)[2:].zfill(k))
        initOnes = binS.count("1")
        if initOnes % 2 != int(s[0]):
            continue
        # print("MASK START", mask)
        for i in range(1, n - k + 1):
            if s[i] == s[i - 1]:
                binS.append(binS[i - 1])
            else:
                if binS[i - 1] == "0":
                    binS.append("1")
                else:
                    binS.append("0")
        cur = binS.count("1")
        # print(binS)
        mx = max(mx, cur)
        mn = min(mn, cur)
    print(mn, mx)
for _ in range(tc):
    solve()
