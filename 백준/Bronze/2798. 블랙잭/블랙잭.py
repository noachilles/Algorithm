n, m = map(int, input().split())
array = list(map(int, input().split()))
res = sum = 0

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum += array[i]
            sum += array[j]
            sum += array[k]
            if sum <= m:
                res = max(res, sum)
            sum = 0
print(res)