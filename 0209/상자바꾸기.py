t = int(input())

for tc in range(1, t + 1):

    n, q = map(int, input().split())
    change = []
    # q번만큼 L R 값을 입력받아 리스트 형태로 저장
    for number in range(q):
        change.append(list(map(int, input().split())))

    # 모든 숫자가 0인 박스 n개 생성
    result = list('0'*n)

    # i가 1일 때부터 q번만큼 진행
    for i in range(1, q+1):
        # i=1에 해당하는 리스트값의 범위만큼
        for j in range(change[i-1][0], change[i-1][1]+1):
            # 주어진 인덱스의 값을 i로 변환
            result[j-1] = i


    print(f'#{tc}', end=' ')
    for r in result:
        print(r, end=' ')

    print()



