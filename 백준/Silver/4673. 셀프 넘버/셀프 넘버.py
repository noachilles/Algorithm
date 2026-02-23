def d(n):
    if n > 9999:
        l = 5
    elif n > 999:
        l = 4
    elif n > 99:
        l = 3
    elif n > 9:
        l = 2
    else:
        l = 1
    res = n
    while l > 0:
        k = (10 ** (l-1))
        res += (n // k)
        n %= k
        # print(l, res)
        l -= 1
    return res

ref = dict()
for x in range(1, 10001):
    if d(x) < 10001:
        ref[d(x)] = 0
for x in range(1, 10001):
    if not x in ref:
        print(x)