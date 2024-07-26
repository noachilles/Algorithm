# (입력)
# (큰 수, N) (나누어질 숫자, K)
# 1)수 N에서 1을 빼고, 
# 2)그 값이 K의 배수일 때 K로 나눈다. 
# (출력)
# N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수

## 1 
# n, k = map(int, input().split())
# res = 0
# while n > 1:
#     if n % k == 0:
#         n /= k
#         res += 1
#     else:
#         n -= 1
#         res += 1
# print(res)

# 단, n < k인 상황을 고려하지 않음

## 2
n, k = map(int, input().split())
res = 0

while True:
    target = (n // k) * k
    res += (n - target)
    n = target
    
    if n < k:
        break
    # n < k 전까지는 k로 나누기
    res += 1
    n //= k

# 이거 왜 빼는 거지?
# 모든 수에 적용되는지는 모르겠으나 (17, 4)를 입력했을 때 n이 1이 되면 target이 0이 됨
# 그래서 res 결과값이 정답보다 1 커짐
res += (n - 1)
print(res)