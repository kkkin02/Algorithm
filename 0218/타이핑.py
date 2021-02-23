t = int(input())

for tc in range(1, t+1):
    A, B = map(list, input().split())
    n = len(A)
    m = len(B)

    for i in range(n-m+1):
        if B == A[i:i+m]:
            A[i:i+m] = '1'

    print(f'#{tc} {len(A)}')


