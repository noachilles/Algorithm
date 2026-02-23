N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

data = sorted(data, reverse=True)
ans = data[0]

for i in range(1, N):
    temp = data[i]
    # 십시일반 케이스를 고려하지 못했다
    if temp * (i+1) > ans:
        ans = temp * (i+1)
print(ans)