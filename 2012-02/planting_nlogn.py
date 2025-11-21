# so uh, I don't think that works (as expected)

# class SegmentTree:
#     def __init__(self, ys):
#         """
#         ys = sorted list of compressed y-coordinates (including endpoints)
#         Leaves correspond to intervals [ys[i], ys[i+1]).
#         """
#         self.y = ys
#         self.n = len(ys) - 1  # number of leaf intervals

#         # tree size
#         self.size = 1
#         while self.size < self.n:
#             self.size *= 2

#         # cover-count and covered length arrays
#         self.cover = [0] * (2 * self.size)
#         self.covered_len = [0] * (2 * self.size)

#     # recompute covered_len[x] from children or cover count
#     def pull(self, x, lx, rx):
#         if self.cover[x] > 0:
#             # interval is fully covered
#             self.covered_len[x] = self.y[rx] - self.y[lx]
#         else:
#             if rx - lx == 1:
#                 # leaf with no cover
#                 self.covered_len[x] = 0
#             else:
#                 # sum of children
#                 self.covered_len[x] = (
#                     self.covered_len[2*x+1] +
#                     self.covered_len[2*x+2]
#                 )

#     # add v (+1 or -1) to interval [l, r)
#     def update(self, l, r, v, x, lx, rx):
#         if r <= lx or rx <= l:
#             return
#         if l <= lx and rx <= r:
#             # whole segment covered
#             self.cover[x] += v
#             self.pull(x, lx, rx)
#             return

#         m = (lx + rx) // 2
#         self.update(l, r, v, 2*x+1, lx, m)
#         self.update(l, r, v, 2*x+2, m, rx)
#         self.pull(x, lx, rx)

#     # public update
#     def range_add(self, l, r, v):
#         self.update(l, r, v, 0, 0, self.size)

#     # query total covered length (root)
#     def total_covered_length(self):
#         return self.covered_len[0]

# import sys
# # sys.stdin = open("planting.in")
# input = sys.stdin.readline

# n = int(input())
# rectangles = [tuple(map(int, input().split())) for _ in range(n)]
# # upper left, lower right corners, sort by x value
# rectangles.sort(key = lambda x: (-x[1], x[0]))
# # print(rectangles)
# events = set()
# for i in range(n):
#     events.add(rectangles[i][0])
#     events.add(rectangles[i][2])
# events = sorted(list(events))

# # Suppose we have intervals like:
# # rectangles = [(x1, y1, x2, y2), ...]
# # First compress y-coordinates:
# ys = sorted({y1 for (_,y1,_,_) in rectangles} |
#             {y2 for (_,_,_,y2) in rectangles})
# # Example: ys = [0, 2, 4, 6]

# # Build the tree
# st = SegmentTree(ys)

# # sweep events:
# # events = [(x, +1, y1, y2), (x, -1, y1, y2), ...]
# # sorted by x
# events.sort()

# prev_x = events[0][0]
# area = 0

# for x, typ, y1, y2 in events:
#     dx = x - prev_x
#     # add the covered y-length * dx
#     area += st.total_covered_length() * dx
#     prev_x = x

#     # apply update
#     # convert y1,y2 to compressed indices
#     l = bisect_left(ys, y1)
#     r = bisect_left(ys, y2)
#     st.range_add(l, r, typ)

# print(area)

