t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    #한 행에서 1의 개수를 더한 것이 사각형의 가로
    rectangle = []
    for i in range(n):
        width = 0
        for j in range(n):
            if arr[i][j] == 1:
                width += 1
        if width != 0:
            rectangle.append(width)

    #리스트에서 같은 가로 값을 카운트한 것이 세로
    max_rec = rectangle[-1] * rectangle.count(rectangle[-1])
    #리스트에 다른 가로 값이 있다면
    for r in range(len(rectangle)-1):
        if rectangle[r] != rectangle[r + 1]:
            #그 가로 값의 세로를 구해 넓이를 비교
            if rectangle[r] * rectangle.count(rectangle[r]) > max_rec:
                max_rec = rectangle[r] * rectangle.count(rectangle[r])

    print('#{} {}'.format(tc, max_rec))
