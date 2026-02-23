N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

coins = sorted(coins, reverse=True)

temp = K
ans = 0
for now in coins:
    if temp >= now:
        ans += temp // now
        temp = temp % now

print(ans)