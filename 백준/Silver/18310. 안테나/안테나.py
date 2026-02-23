n = int(input())
data = list(map(int, input().split()))
data.sort()
# avg = int(sum(data) / n) # 평균 X, 중앙값 사용해야 함
mid = 0
if n % 2 == 0:
    mid = data[int(n / 2) - 1]
else:
    mid = data[int(n / 2)]

def divide(data, key):
    if n <= 1:
        return key
    for i in range(1, n):
        if data[i] > key:
            smaller = data[:i]
            bigger = data[i:]
            break
    if abs(key - smaller[-1]) > abs(key - bigger[0]): # 작은 값이 큰 값보다 평균과 차이가 크면
        return bigger[0]
    else:
        return smaller[-1]

# res2 = divide(data, mid)
print(mid)