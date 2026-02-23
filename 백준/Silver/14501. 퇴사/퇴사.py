N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if (N-i) < T[i][0]:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+T[i][0]] + T[i][1])
print(dp[0])