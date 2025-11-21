n, k = map(int, input().split())
# n = 7
# k = 3

# math.comb will be useful here
import math

# could be implemented like a segment tree -- as we add numbers, converge on a segment
def f(digits, p, z, k):
    digits -= 1
    k -= 1

    # z zeros, k ones
    # print(digits, z, k, p)

    ret = "1"
    total = math.comb(digits, z)

    # keep track of k & z to see what's left
    L = 1
    R = total
    while digits != 0:
        if k == 0:
            ret += "0"
            z -= 1
            digits -= 1
            continue
        if z == 0:
            ret += "1"
            k -= 1
            digits -= 1
            continue
        # choose 0
        newL = L
        newR = L + math.comb(digits - 1, z - 1) - 1
        # print(newL, newR)
        if p >= newL and p <= newR:
            ret += "0"
            z -= 1
            L = newL
            R = newR
        else:
            newL = R - math.comb(digits - 1, k - 1) + 1
            newR = R
            ret += "1"
            k -= 1
            L = newL
            R = newR
        digits -= 1
    
    return ret

t = 1
digits = k
while t < n + 1:
    slots = digits - 1
    allCombos = math.comb(slots, k - 1)
    # print(allCombos)
    if t + allCombos > n:
        rem = n - t
        permutationNumber = rem + 1
        zeros = digits - k
        # print("digits:", digits, "permutation:", permutationNumber)
        ans = f(digits, permutationNumber, zeros, k)
        print(ans)
        exit()
    t += allCombos
    digits += 1

'''
obviously need some sort of speedup mechanism
ex. k = 3
digits = 3: 1 11 2C2
digits = 4: 1 011, 1 101, 1 110 | 2 1's & 1 0 to arrange, 3C2
digits = 5: | 2 1's & 2 0's to arrange, 4C2

1/3/6
1, 2-4, 5-10

then it boils down to the permutation problem
after fast-forwarding, procedurally iteration through the permutations? turing-machine like
    nvm, maybe not enough time
    ex. start w/
    0011 <-- 1C1
    0101
    0110 <-- 2C1
    1001
    1010
    1100 <-- 3C1
thoughts: recursive algorithm, how many permutations come after this one
solve kth permutation after this (related problem)
'''
