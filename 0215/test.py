t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1<<n):
        sub = []
        for j in range(n):
            if i & (1<<j):
                sub.append(arr[j])

    print(sub)