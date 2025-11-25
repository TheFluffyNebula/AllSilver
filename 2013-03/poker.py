import sys
sys.stdin = open("poker.in")
sys.stdout = open("poker.out", 'w')
input = sys.stdin.readline

n = int(input())
cards = [0] + [int(input()) for _ in range(n)]
# print(cards)
ans = 0
for i in range(1, n + 1):
    if cards[i] > cards[i - 1]:
        ans += cards[i] - cards[i - 1]
print(ans)

'''
wild guess
oh!
'''
