import sys
sys.stdin = open("hps.in")
sys.stdout = open("hps.out", 'w')

def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    lookup = {b'H': 0, b'P': 1, b'S': 2}
    g_arr = [lookup[data[2 + i]] for i in range(n)]
    
    prev = [0] * (3 * (k + 1))
    for g in range(3):
        prev[g] = 1 if g_arr[0] == g else 0
    
    for i in range(1, n):
        gi = g_arr[i]
        w0 = 1 if gi == 0 else 0
        w1 = 1 if gi == 1 else 0
        w2 = 1 if gi == 2 else 0
        curr = [0] * (3 * (k + 1))
        curr[0] = prev[0] + w0
        curr[1] = prev[1] + w1
        curr[2] = prev[2] + w2
        for j in range(1, k + 1):
            b = j * 3
            pb = b - 3
            p0, p1, p2 = prev[pb], prev[pb + 1], prev[pb + 2]
            # keep
            a0 = prev[b] + w0
            a1 = prev[b + 1] + w1
            a2 = prev[b + 2] + w2
            # swap into g from either of the other two
            s0 = (p1 if p1 > p2 else p2) + w0
            s1 = (p0 if p0 > p2 else p2) + w1
            s2 = (p0 if p0 > p1 else p1) + w2
            curr[b]     = a0 if a0 > s0 else s0
            curr[b + 1] = a1 if a1 > s1 else s1
            curr[b + 2] = a2 if a2 > s2 else s2
        prev = curr
    
    print(max(prev))

main()