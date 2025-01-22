# boj 11047
# (입력)
# (동전 종류, N) (가치의 합, 목표값, K)
# (N개의 줄에 동전 가치-오름차순, Ai)
# (출력)
# 필요한 동전 개수 최솟값

n, k = map(int, input().split())
ai = [0 for i in range(n)]
res = 0
for i in range(n):
    ai[i] = int(input())

while k > 0:
    for i in range(n-1, -1, -1):
        if ai[i] > k:
            continue
        res += (k // ai[i])
        k -= ((k // ai[i]) * ai[i])
        # print("{}번째 동전까지 뺀 값은 {}입니다.".format(i, k))
print(res)
        