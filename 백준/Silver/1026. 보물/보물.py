N = int(input())
A = list(map(int, input().split()))[:N]
B = list(map(int, input().split()))[:N]

A = sorted(A)
B = sorted(B, reverse = True)

ans = 0

for i in range(N):
    ans += A[i] * B[i]

print(ans)