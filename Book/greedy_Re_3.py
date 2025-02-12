# 설명
# N이 1이 될 때까지 두 과정 중 하나를 반복
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다 (나누어 떨어질 때만)
# 수행 최소 횟수
n, k = map(int, input().split())
res = 0
while n >= k:
    while n % k != 0:
        n -= 1
        res += 1
    n //= k
    res += 1
while n > 1:
    n -= 1
    res += 1
    
print(res)

while n > 1:
    if n % k != 0:
        n //= k
        res += 1
    else:
        n -= 1
        res += 1
print(res)
    