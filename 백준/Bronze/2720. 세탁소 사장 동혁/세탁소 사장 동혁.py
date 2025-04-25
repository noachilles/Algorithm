T = int(input())

for test_case in range(T):
    change = int(input())
    res = [0] * 4
    while change:
        if change >= 25:
            res[0] += change // 25
            change %= 25
        elif change >= 10:
            res[1] += change // 10
            change %= 10
        elif change >= 5:
            res[2] += change // 5
            change %= 5
        else:
            res[3] += change
            change = 0
    for i in range(4):
        print(res[i], end=' ')
    print()