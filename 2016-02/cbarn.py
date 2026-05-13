import sys
sys.stdin = open("cbarn.in")
# sys.stdout = open("cbarn.out", 'w')

n = int(input())
cows = [int(input()) for _ in range(n)]
print(cows)

'''
instead of mapping cows to sinks, 
what if we look at each sink and have it take the closest cow?
'''
