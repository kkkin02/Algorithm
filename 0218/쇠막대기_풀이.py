t = int(input())

for tc in range(1, t+1):
    bar = input()

    cnt = 0
    result = 0

    for i in range(len(bar)):
        #열린 괄호면 막대 개수 추가
        if bar[i] == '(':
            cnt += 1
        #닫힌 괄호면 막대 개수 감소
        else:
            cnt -= 1

            #닫힌 괄호인데 전이 열린괄호였으면 레이저
            if bar[i-1] == '(':
                #그때까지 누적된 막대기들이 잘린거니까
                result += cnt

            #레이저가 아니면 막대가 끝난거니까
            else:
                result += 1
    print(f'#{tc} {result}')