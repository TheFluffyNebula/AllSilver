import sys
sys.stdin = open("haybales.in")
sys.stdout = open("haybales.out", 'w')

n, q = map(int, input().split())
bales = list(map(int, input().split()))
bales.sort()

def query(start, end):
    # todo: ask how bisect would work
    L = 0
    R = n - 1
    sIdx = -1
    while L <= R:
        mid = (L + R) // 2
        if bales[mid] >= start:
            sIdx = mid
            R = mid - 1
        else:
            L = mid + 1

    L = 0
    R = n - 1
    eIdx = -1
    while L <= R:
        mid = (L + R) // 2
        if bales[mid] <= end:
            eIdx = mid
            L = mid + 1            
        else:
            R = mid - 1

    if sIdx == -1 or eIdx == -1:
        return 0
    return eIdx - sIdx + 1

for _ in range(q):
    a, b = map(int, input().split())
    print(query(a, b))
