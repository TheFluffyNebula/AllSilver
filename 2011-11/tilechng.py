import sys
# sys.stdin = open("tilechng.in")
input = sys.stdin.readline
import math

n, m = map(int, input().split())
tiles = [int(input()) for _ in range(n)]

if len(tiles) > m:
    print(-1)
    exit()

tiles.sort()
# print(tiles)

# n = 7
# m = 28

solutions = []
curSolution = []

def backtrack(curSum, curList):
    if curSum > m:
        return
    if len(curList) == n:
        if curSum == m:
            solutions.append(curList.copy())
        return

    rem = math.floor(math.sqrt(m - curSum))
    if len(curList) == 0:
        start = 1
    else:
        start = curList[-1]
    for i in range(start, rem + 1):
        curList.append(i)
        backtrack(curSum + i ** 2, curList)
        curList.pop()

backtrack(0, curSolution)
# print(solutions)

if len(solutions) == 0:
    print(-1)
    exit(0)

best = float('inf')

for solution in solutions:
    cur = sum(abs(solution[i] - tiles[i]) ** 2 for i in range(n))
    best = min(best, cur)

print(best)

'''
differences are always differences of squares (a + b)(a - b)
each update has a different cost -- graph approach?

backtracking algorithm, take best? 
surely can't have that many options since we can automatically prune once it goes over
(can't go back under)

sort tiles, greedily work towards result?
ex. start at 19, options to go down:
3 -> 2 (-5)
3 -> 1 (-8)
(cost: 4, change: -8)
(cost: 1, change: -5) -> cost(3, change: -3)

how about seeing if a solution is present in the first place
can there be multiple solutions?
ex. 4 tiles, sum = 28
25 + 1 + 1 + 1
9 + 9 + 9 + 1
oh. hmmm
what about, generating possible solutions through backtracking?
prune permutations via only letting numbers be same or more than the previous
for each successful solution, calculate the difference optimally (sort the tiles)

**at least try these approaches before peeking the solution**
'''

'''
backtracking pseudocode:
function backtrack(candidate_solution):
    if reject(candidate_solution):
        return // Prune the search space
    
    if accept(candidate_solution):
        output(candidate_solution) // Found a solution, process it
        // Optionally, return if only one solution is needed
    
    // Generate extensions for the current candidate
    for each extension in generate_candidates(candidate_solution):
        // Make a move (add the extension to the candidate solution)
        make_move(candidate_solution, extension) 
        
        // Recursively explore this extended path
        backtrack(candidate_solution)
        
        // Unmake the move (remove the extension to backtrack)
        undo_make_move(candidate_solution, extension)
'''
