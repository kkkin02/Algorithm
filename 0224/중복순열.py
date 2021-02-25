# 원래 주어진 숫자열 길이와 같은 중복순열들을 만들 때

def f(n, k): # n 숫자를 채울 인덱스, k 숫자를 채워넣을 p의 크기
    if n==k: # 중복순열 완성
        print(p)
    else:
        for i in range(1, k+1):
            p[n] = i
            f(n+1, k)


N = 3
p = [0] * N
f(0, N)
