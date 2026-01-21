import sys
# sys.stdin = open("c.in")

'''
observation: 
    when r_i == r_i-1, the bit that enters must be equal to the bit that leaves
    when they're different, enter bit != leaving bit

let's run with this observation!
intervals, ex. see what's optimal for each set of slots
ex. for k = 3, 1&4 are linked, 2&5 are linked
for all sets, add up the greatest frequency
for the other problem, add up least frequency

leave no-link last & greedily fill that way
'''

tc = int(input())

def solve():
    n, k = map(int, input().split())
    # print(n, k)
    s = input().strip()
    if k == 1:
        print(s.count("1"), s.count("1"))
        return
    # status for picking 0, status2 for picking 1
    status = [-1] * n
    status2 = [-1] * n
    
    startPoints = min(k, n - k)
    # freq[i][0] = 0's starting from i, freq[i][1] = 1's starting from i
    freq = [[0 for _ in range(2)] for _ in range(startPoints)]
    for i in range(k, n):
        prev = i - k
        if status[prev] == -1:
            # set 0 first
            status[prev] = 0
        if status2[prev] == -1:
            # set 1 first
            status2[prev] = 1
            freq[i % k][1] = 1
        if s[prev] == s[prev + 1]:
            status[i] = status[prev]
            status2[i] = status2[prev]
        else:
            status[i] = 1 - status[prev]
            status2[i] = 1 - status2[prev]
        freq[i % k][0] += status[i]
        freq[i % k][1] += status2[i]
    # print(status, status2)

    # unused = [0, 1]
    unused = status.count(-1)
    for _ in range(unused):
        freq.append([0, 1])
    freq.sort(key = lambda x: abs(x[0] - x[1]), reverse=True)
    # print(freq)

    mn = 0
    mx = 0
    mn_residue = 0
    mx_residue = 0
    for i in range(k):
        if i == k - 1:
            if mn_residue == int(s[0]):
                mn += freq[i][0]
            else:
                mn += freq[i][1]
            if mx_residue == int(s[0]):
                mx += freq[i][0]
            else:
                mx += freq[i][1]
            break
        if freq[i][0] >= freq[i][1]:
            mn += freq[i][1]
            mx += freq[i][0]
            mn_residue = 1 - mn_residue
        else:
            mn += freq[i][0]
            mx += freq[i][1]
            mx_residue = 1 - mx_residue
    print(mn, mx)
for _ in range(tc):
    solve()
