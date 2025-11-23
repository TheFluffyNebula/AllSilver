import sys
sys.stdin = open("squares.in")
# sys.stdout = open("squares.out", 'w')
input = sys.stdin.readline

n, k = map(int, input().split())
squares = [tuple(map(int, input().split())) for _ in range(n)]
squares.sort()
print(squares)



'''
probably some sorting for more efficient comparisons
by x, then by y
for each square maintain all points within k units horizontally
ex. k = 2 --> squares within 1 away qualify
    k = 4 --> squares within 3 away
for all of these squares, for each new square that enters the window, 
need to find if there are any that are less than k away vertically
binary search tree data structure likely works
'''
