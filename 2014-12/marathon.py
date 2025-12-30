import sys
sys.stdin = open("marathon.in")
# sys.stdout = open("marathon.out", 'w')

n, k = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

'''
dp(i, skips) = min distance at checkpoint i using [skips] skips
'''
