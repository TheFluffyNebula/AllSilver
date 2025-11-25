# AC!
import sys
sys.stdin = open("tractor.in")
sys.stdout = open("tractor.out", 'w')
input = sys.stdin.readline

class DisjointSets:
	def __init__(self, size: int) -> None:
		self.parents = [i for i in range(size)]
		self.sizes = [1 for _ in range(size)]

	def find(self, x: int) -> int:
		""":return: the "representative" node in x's component"""
		if self.parents[x] == x:
			return x
		self.parents[x] = self.find(self.parents[x])
		return self.parents[x]

	def unite(self, x: int, y: int) -> bool:
		""":return: whether the merge changed connectivity"""
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root == y_root:
			return False

		if self.sizes[x_root] < self.sizes[y_root]:
			x_root, y_root = y_root, x_root

		self.parents[y_root] = x_root
		self.sizes[x_root] += self.sizes[y_root]
		return True

	def connected(self, x: int, y: int) -> bool:
		""":return: whether x and y are in the same connected component"""
		return self.find(x) == self.find(y)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

edges = []
for i in range(n):
	for j in range(n):
		a = n * i + j
		if i > 0:
			b = n * (i - 1) + j
			w = abs(board[i][j] - board[i - 1][j])
			edges.append((w, a, b))
		if j > 0:
			b = n * i + j - 1
			w = abs(board[i][j] - board[i][j - 1])
			edges.append((w, a, b))
			
edges.sort()
# print(*[edges[i].weight for i in range(len(edges))])

dsj_set = DisjointSets(n ** 2)

half = (n ** 2) // 2
if n % 2 == 1:
	half += 1

for e in edges:
    if dsj_set.find(e[1]) != dsj_set.find(e[2]):
        dsj_set.unite(e[1], e[2])
        if dsj_set.sizes[dsj_set.parents[e[1]]] >= half or dsj_set.sizes[dsj_set.parents[e[2]]] >= half:
            print(e[0])
            exit()
