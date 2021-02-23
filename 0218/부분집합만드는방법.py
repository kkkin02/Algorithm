n = 3
a = [x for x in range(1, n+1)]

subset = [[]]
for i in a:
    size = len(subset)
    for j in range(size):
        subset.append(subset[j]+[i])

print(subset)
