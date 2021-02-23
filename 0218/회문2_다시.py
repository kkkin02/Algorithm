t = 10

for tc in range(1, t + 1):
    input()
    arr = []
    for _ in range(100):
        arr.append(input())

    print(f'#{tc}', end=' ')
    max_pal = 1
    for i in range(100):
        for j in range(99):
            for k in range(j, 100):
                #가로탐색
                word_hor = arr[i][j:k+1]
                if word_hor == word_hor[::-1]:
                    if k-j+1 > max_pal:
                        max_pal = k-j+1

    #세로로된 문자열 만들기
    vertical = []
    for a in range(100):
        string = ''
        for b in range(100):
            string += arr[b][a]
        vertical.append(string)

    for i in range(100):
        for j in range(99):
            for k in range(j, 100):
                #세로탐색
                word_ver = vertical[i][j:k+1]
                if word_ver == word_ver[::-1]:
                    if k-j+1 > max_pal:
                        max_pal = k-j+1


    print(max_pal)