
def f(idx, k, s): # n 은 숫자를 채울 인덱스, k 는 생성할 순열의 크기, s는 순열의 합
    global min_v
    if idx == k: # 순열 완성
        if min_v > s:
            min_v = s
            return

    elif min_v <= s: # 어차피 최소를 찾는거니까 그냥 끝내
        return

    else:
        for i in range(k): # 사용할 숫자가 남아있으면
            if used[i] == 0:
                used[i] = 1
                f(idx+1, k, s+arr[idx][i])
                # 초기화
                used[i] = 0


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    min_v = 90
    used = [0] * n

    f(0, n, 0)

    print(f'#{tc} {min_v}')