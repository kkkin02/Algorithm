def f(n, k, v): # n 접근할 인덱스, k 배열의 크기, v 찾으려는 수
    if n == k: # 배열을 벗어난 경우(끝까지 봤는데도 찾으려는 수가 없는 경우)
        return 0
    elif A[n] == v: # 찾은 경우
        return 1
    else:
        return f(n+1, k, v) # 배열을 벗어나지 않았고, 찾는 숫자도 아닌 경우


A = [7, 2, 4, 3, 5, 8]
N = len(A)
print(f(0, N, 5))
print(f(0, N, 9))