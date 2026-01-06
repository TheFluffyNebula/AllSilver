# original got AC but let's make a binary tree for the intended TC
import sys
sys.stdin = open("stampede.in")
sys.stdout = open("stampede.out", 'w')
from collections import defaultdict

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self, val):
        if not self.root:
            self.root = Node(val)
            return
        cur = self.root
        while True:
            if val <= cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    return
        
    def remove(self, val):
        cur = self.root
        parent = None
        while cur and cur.val != val:
            parent = cur
            if val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right
        # if not cur: return
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                self.root = child
            elif parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        else:
            succ_parent = cur
            succ = cur.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            cur.val = succ.val
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
    
    def min(self):
        if not self.root:
            return -1
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
# print(cows)

add = defaultdict(list)
rm = defaultdict(list)
pts = set()
# intervals = []
for i in range(n):
    reachZero = -(cows[i][0] + 1) * cows[i][2]
    endZero = reachZero + cows[i][2]
    # intervals.append((reachZero, endZero, cows[i][1]))
    add[reachZero].append(cows[i][1])
    rm[endZero].append(cows[i][1])
    pts.add(reachZero)
    pts.add(endZero)
pts = sorted(list(pts))
# print(pts, add, rm)

seen = set()
bt = BinaryTree()
for p in pts:
    put = add[p]
    remove = rm[p]
    if put:
        for insertElement in put:
            # ADD insertElement to the tree
            bt.add(insertElement)
    if remove:
        for removeElement in remove:            
            # REMOVE insertElement from the tree
            bt.remove(removeElement)
    btMin = bt.min()
    if btMin != -1:
        seen.add(btMin)

# print(seen)
print(len(seen))

'''
cows being represented by line segments make this a lot trickier
is there a way to simulate this quickly?

priority queue/binary tree, smallest one at any time is able to be seen
store by y-coordinates (unique)
add when we get to L, remove when we get to R

ok, I think it's finally time to make a binary tree implementation
'''
