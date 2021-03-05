# 일단 부분집합 다 만들어놓고 판단하는 방법

t = int(input())

for tc in range(1, t+1):
    n, calorie = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    hamburger = [[]]

    for x in info:
        size = len(hamburger)
        for y in range(size):
            hamburger.append(hamburger[y]+[x])

    max_score = 0
    for i in hamburger:
        score = 0
        cal = 0
        for j in i:
            score += j[0]
            cal += j[1]
            if cal <= calorie and score > max_score:
                max_score = score

    print(f'#{tc} {max_score}')




