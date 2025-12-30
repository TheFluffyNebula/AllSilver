import sys
sys.stdin = open("cowjog.in")
# sys.stdout = open("cowjog.out", 'w')

n, t = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()

'''
could tackle this problem by iterating in reverse order
"will cow i+1 catch up to cow i"
then if it does, move onwards
'''
