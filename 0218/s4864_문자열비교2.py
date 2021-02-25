t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    m = len(str1)
    n = len(str2)

    for i in range(n-m+1):
        if str2[i:i+m] == str1:
            print(f'#{tc} 1')
            break

    else:
        print(f'#{tc} 0')
