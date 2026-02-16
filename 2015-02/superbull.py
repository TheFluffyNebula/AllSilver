import sys
sys.stdin = open("superbull.in")
sys.stdout = open("superbull.out", 'w')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
# print(nums)

ans = 0
inMST = [False] * n
max_e = [0] * n
# put nodes 1, 2, ..., n - 1 into the tree
for i in range(n):
    u = -1
    for v in range(n):
        if not inMST[v] and (u == -1 or max_e[v] > max_e[u]):
            u = v
    
    inMST[u] = True
    ans += max_e[u]
    
    for v in range(n):
        alt = nums[u] ^ nums[v]
        if not inMST[v] and alt > max_e[v]:
            max_e[v] = alt
print(ans)
'''
maximum spanning tree
heapless prim's because the graph is complete
'''
