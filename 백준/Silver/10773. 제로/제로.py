a = []
res = 0
last = 0
k = int(input())
for _ in range(k):
    n = int(input())
    if n == 0:
        res -= last
        a.pop()
        if a:
            last = a[-1]
        continue
    a.append(n)
    res += n
    last = a[-1]
print(res)