def findpage(p, fp):
    start = 1
    end = p
    cnt = 1
    while start <= end:
        middle = (start + end) // 2
        if middle == fp:
            return cnt
        elif middle < fp:
            start = middle
            cnt += 1
        else:
            end = middle
            cnt += 1
    return cnt

t = int(input())

for tc in range(1, t+1):
    print(f'#{tc}', end=' ')

    p, pa, pb = map(int, input().split())
    if findpage(p, pa) > findpage(p, pb):
        print('B')
    elif findpage(p, pa) < findpage(p, pb):
        print('A')
    else:
        print(0)



