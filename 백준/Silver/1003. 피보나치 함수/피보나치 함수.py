import sys
input = sys.stdin.readline

t = int(input())
while t:
    res = []
    n = int(input())
    res.append((1, 0))
    res.append((0, 1))
    if n < 2:
        print(res[n][0], res[n][1])
        t -= 1
        continue
    for i in range(2, n+1):
        num_0 = res[i-1][0] + res[i-2][0]
        num_1 = res[i-1][1] + res[i-2][1]
        res.append((num_0, num_1))
    print(res[n][0], res[n][1])
    t -= 1