testArray = [1, 2, 3, 2, 1]

# 1's, 2's, 1-4/2-5
tables = [testArray]
print(tables)
x = 2
idx = 1
while x <= len(testArray):
    curList = []
    prevLen = len(tables[idx - 1])
    for i in range(prevLen):
        if i + 2 ** (idx - 1) > prevLen - 1:
            break
        newVal = min(tables[idx - 1][i], tables[idx - 1][i + 2 ** (idx - 1)])
        curList.append(newVal)
    tables.append(curList)
    idx += 1
    x *= 2
print(tables)
