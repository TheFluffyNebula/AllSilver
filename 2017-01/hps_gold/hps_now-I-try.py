# syntax is still a bit fishy but I get the concept at least
# fewer accesses
import sys
sys.stdin = open("hps.in")
sys.stdout = open("hps.out", 'w')

n, k = map(int, input().split())
lookup = {'H': 0, 'P': 1, 'S': 2}
gestures = [lookup[input().strip()] for _ in range(n)]
# print(gestures)

def main():
    # H0, P1, S2
    prev = [[0 for _ in range(3)] for _ in range(k + 1)]
    cur = [[0 for _ in range(3)] for _ in range(k + 1)]
    prev[0][gestures[0]] = 1
    for i in range(1, n):
        gi = gestures[i]
        w0, w1, w2 = int(gi == 0), int(gi == 1), int(gi == 2)
        p = prev[0]
        # j = 0, only option is no swap
        cur[0][0] = p[0] + w0
        cur[0][1] = p[1] + w1
        cur[0][2] = p[2] + w2

        for j in range(1, k + 1):
            same = prev[j]      # same switch count, "keep" transitions
            fewer = prev[j - 1] # one fewer switch, "swap" transitions
            curr = cur[j]
            
            a, b, c = fewer[0], fewer[1], fewer[2]
            
            # For each gesture g: either keep playing g (from `same`)
            # or switch into g from one of the other two gestures (from `fewer`).
            keep_h,  swap_into_h = same[0], b if b > c else c
            keep_p,  swap_into_p = same[1], a if a > c else c
            keep_s,  swap_into_s = same[2], a if a > b else b
            
            curr[0] = (keep_h if keep_h > swap_into_h else swap_into_h) + w0
            curr[1] = (keep_p if keep_p > swap_into_p else swap_into_p) + w1
            curr[2] = (keep_s if keep_s > swap_into_s else swap_into_s) + w2
        prev, cur = cur, prev
    ans = 0
    for j in range(k + 1):
        for g in range(3):
            ans = max(ans, prev[j][g])
    print(ans)
main()

'''
fixes: 
input (didn't actually matter)
rolling dp (faster lookups)
recomputation of gestures[i] == ?, just do it once (some speedup!)
inline the max under comparison (didn't do, will do last if fails)
put in main() function, "local var lookups 2x faster than globals in CPython"
'''
