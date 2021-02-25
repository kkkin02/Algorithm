# 만드려고 하는 중복순열의 길이보다 주어진 숫자가 더 많을 때

def f(n, k, m): # n 숫자를 채울 인덱스, k 숫자를 채워넣을 p의 크기
    if n==k: # 중복순열 완성
        print(p)
    else:
        for i in range(1, m+1):
            p[n] = i
            f(n+1, k, m)

N = 5
p = [0] * 3
f(0, 3, N)