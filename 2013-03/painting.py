import sys
sys.stdin = open("poker.in")
# sys.stdout = open("poker.out", 'w')
input = sys.stdin.readline

n = int(input())
x1, y1, x2, y2 = map(int, input().split())

'''
solution peek: sweep line w/ binary tree
'''
