t = int(input())

for tc in range(1, t+1):
    n = int(input())
    carrots = list(map(int, input().split()))

    section_a = 0
    min_section = 0
    min_diff = 987654321
    for i in range(n):
        section_a += carrots[i]
        section_b = sum(carrots) - section_a
        if abs(section_a - section_b) < min_diff:
            min_diff = abs(section_a - section_b)
            min_section = i+1

    print('#{} {} {}'.format(tc, min_section, min_diff))
