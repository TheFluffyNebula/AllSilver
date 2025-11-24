import sys
sys.stdin = open("msched.in")
# sys.stdout = open("msched.out", 'w')



'''
some ideas:
1. direct simulation (probably too slow)

2. topological sort (not really, more like select degrees w/ 0 in-degree)
    ans = longest path: (node takes max of any path to it)
    use indegree to identify when nodes are ready
'''
