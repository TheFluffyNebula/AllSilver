import sys
sys.stdin = open("b.in")

tc = int(input())

'''
resolve x vars, x constraints situations first
ex. x x z or cycles
then resolve the trees
ignore & +1 if no appearance
'''

def solve():
    n, m = map(int, input().split())
    lower = list(map(int, input().split()))
    upper = list(map(int, input().split()))
    constraints = [list(map(int, input().split())) for _ in range(m)]
    print(lower, upper, constraints)


for _ in range(tc):
    solve()
