N = int(input())
A = list(map(int, input().split()))

A.sort()
if N % 2 == 0:
    i, j = 0, N-1
    ans = A[i] + A[j]
else:
    i, j = 0, N-2
    ans = A[N-1]

while i < j:
    temp = A[i] + A[j]
    if temp > ans:
        ans = temp
    i += 1
    j -= 1
print(ans)