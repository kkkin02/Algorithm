t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    b_range = []
    for number in range(n):
        b_range.append(list(map(int, input().split())))

    p = int(input())
    b_stop = []
    for count in range(p):
        b_stop.append(int(input()))

    bus_stop = [0] * 5000
    for i in range(n):
        for j in range(b_range[i][0], b_range[i][1]+1):
            bus_stop[j-1] += 1

    print(f"#{tc}", end=" ")
    for k in b_stop:
        print(f'{bus_stop[k-1]}', end=" ")
    print()







