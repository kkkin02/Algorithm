t = int(input())

for tc in range(1, t+1):
    original = list(map(int, input()))
    n = len(original)
    current = []
    for _ in range(n):
        current.append(0)

    cnt = 0

    for i in range(n):
        if original[i] == current[i]:
            continue
        else:
            if original[i] == 1:
                for j in range(i, n):
                    current[j] = 1
                cnt += 1
            else:
                for j in range(i, n):
                    current[j] = 0
                cnt += 1


    print(f'#{tc} {cnt}')

