import sys
# sys.stdin = open("photo.in")
input = sys.stdin.readline
from collections import defaultdict

class p:
    def __init__(self, id, indices):
        self.id = id
        self.indices = indices
    
    def __lt__(self, other):
        comesBefore = 0
        for i in range(5):
            if self.indices[i] < other.indices[i]:
                comesBefore += 1
        # print(self.id, self.indices, other.id, other.indices, comesBefore)
        if comesBefore >= 3:
            # comes before
            return True
        # comes after
        return False

n = int(input())
photos = []
for i in range(5):
    cur = []
    for j in range(n):
        x = int(input())
        cur.append(x)
    photos.append(cur)
# print(*photos, sep = '\n')
photoIndices = defaultdict(list)
for i in range(5):
    for j in range(n):
        photoIndices[photos[i][j]].append(j)
        # print(photos[i][j], j)
positions = []
for k, v in photoIndices.items():
    position = p(k, v)
    positions.append(position)
positions.sort()
for position in positions:
    print(position.id)

'''
had to peek the solution:
Solution Notes (Albert Gu): Consider two cows labeled A and B. Suppose that in the original ordering, 
A came before B. Notice that in the five photographs, neither A nor B moved in at least three of them 
(that is, A and B must still be in the correct relative order in at least three of the photographs). 
Given these five photographs, we can just compare the number of times A came before B; if it is three or more, 
then A is before B in the original ordering, otherwise B is before A in the original ordering. 
This provides us with a fast comparison function between any two cows. 
Now all that is left is sorting all the cows using this comparator.

ohh, I didn't realize that they were all moving from the original ;-;
I kinda thought about it?
even given this, it seems slightly challenging to implement

nevermind, looks like the custom comparator is simply the way to go ._.
'''
