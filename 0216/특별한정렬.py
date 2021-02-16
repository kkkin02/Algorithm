t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 일단 정렬하기 (버블정렬)
    for i in range(n-1):
        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    # 정렬한 리스트를 반으로 나누기
    numbers_l = numbers[:n//2]
    numbers_r = numbers[n//2:]
    # 큰쪽 리스트를 내림차순으로 정렬
    numbers_r = numbers_r[::-1]

    # 반복문을 돌면서 작은쪽 리스트의 짝수번 인덱스에 큰쪽 리스트를 삽입
    for k in range(0, n//2):
        numbers_l.insert(k * 2, numbers_r[k])
    # 만약 n이 홀수라면 numbers_r의 가장 작은 수를 마지막에 삽입
    if n % 2:
        numbers_l.append(numbers_r[-1])


    print(f'#{tc}', end=' ')
    print(*numbers_l[:10])
