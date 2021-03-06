t = 10

for tc in range(1, t+1):
    n = int(input())
    box = list(map(int, input().split()))

    for i in range(n):
        max_idx = min_idx = 0
        max_b = min_b = box[0]

        for idx, j in enumerate(box):
            if j > max_b:
                max_b = j
                max_idx = idx

            elif j < min_b:
                min_b = j
                min_idx = idx

        box[max_idx] -= 1
        box[min_idx] += 1

    result = max(box) - min(box)
    print(f'#{tc} {result}')



