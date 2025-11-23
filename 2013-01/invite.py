import sys
sys.stdin = open("invite.in")
sys.stdout = open("invite.out", 'w')
input = sys.stdin.readline
from collections import defaultdict

n, g = map(int, input().split())
groups = [[] for _ in range(g)]
counts = [0] * g
presence = defaultdict(list)
for i in range(g):
    a = list(map(int, input().split()))
    counts[i] = a[0]
    groups[i] = a[1:]
    for element in groups[i]:
        presence[element].append(i)
# print(groups)
# print(counts)
# print(presence)

# start with 1
changes = [1]
ans = set()
invited = [False] * (n + 1)
invited[1] = True
while changes:
    e = changes.pop()
    ans.add(e)
    for p in presence[e]:
        counts[p] -= 1
        if counts[p] == 1:
            for member in groups[p]:
                if not invited[member]:
                    invited[member] = True
                    changes.append(member)
                    break
print(len(ans))

'''
hmm, interesting!
I'll try slightly-more-careful brute force first
-1 until we hit 1, then operate on next
once there are no 1's we're done
'''
