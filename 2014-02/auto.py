import sys
sys.stdin = open("auto.in")
sys.stdout = open("auto.out", 'w')

w, q = map(int, input().split())
words = [input().strip() for _ in range(w)]
wordToIdx = dict()
for (i, word) in enumerate(words):
    wordToIdx[word] = i + 1

queries = [input().split() for _ in range(q)]
n = len(words)
words.sort()
# print(words, queries)

for k, prefix in queries:
    k = int(k)
    pn = len(prefix)
    # print(k, prefix)
    
    L = 0
    R = n - 1
    trueL = -1
    while L <= R:
        mid = (L + R) // 2
        substring = words[mid][:pn]
        if substring == prefix:
            trueL = mid
            R = mid - 1
        elif substring < prefix:
            L = mid + 1
        else:
            R = mid - 1
    
    L = 0
    R = n - 1
    trueR = -1
    while L <= R:
        mid = (L + R) // 2
        substring = words[mid][:pn]
        if substring == prefix:
            trueR = mid
            L = mid + 1
        elif substring < prefix:
            L = mid + 1
        else:
            R = mid - 1

    totWithPrefix = trueR - trueL + 1
    if k > totWithPrefix or trueL == -1:
        print(-1)
    else:
        word = words[trueL + (k - 1)]
        print(wordToIdx[word])

'''
binary searches on prefix to locate L and R
'''
