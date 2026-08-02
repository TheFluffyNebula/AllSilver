# based on the official solution
# isolate 12 pts, 3 each on the extremes, feasibility check is O(12) instead of O(n)
by_x = sorted(cows, key=lambda p: p[0])
by_y = sorted(cows, key=lambda p: p[1])
xs_sorted = [p[0] for p in by_x]  # for looking up the 4 candidate coords
ys_sorted = [p[1] for p in by_y]

candidates = set(by_x[:3]) | set(by_x[-3:]) | set(by_y[:3]) | set(by_y[-3:])

best = float('inf')
for lo_x_r in range(4):
    for hi_x_r in range(4):
        for lo_y_r in range(4):
            for hi_y_r in range(4):
                lo_x = xs_sorted[lo_x_r]
                hi_x = xs_sorted[n - 1 - hi_x_r]
                lo_y = ys_sorted[lo_y_r]
                hi_y = ys_sorted[n - 1 - hi_y_r]
                if lo_x > hi_x or lo_y > hi_y:
                    continue
                outside = sum(
                    1 for p in candidates
                    if p[0] < lo_x or p[0] > hi_x or p[1] < lo_y or p[1] > hi_y
                )
                if outside <= 3:
                    best = min(best, (hi_x - lo_x) * (hi_y - lo_y))