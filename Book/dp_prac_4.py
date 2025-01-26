# 설명
# N종류 화폐 개수를 최소한으로 -> 가치 합이 M원이 되도록

# 입력
# N(화폐 종류수), M(target)
# N줄 ~ 화폐 가치
# 출력
# 최소한의 화폐 개수(순서 달라도 내용 같으면 같은 걸로)
# 불가능하면 -1

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()
# print(array)
d = [10001] * 10000

for k in array:
    d[k] = 1
    
for i in range(array[0], m+1):
    for k in array:
        d[i] = min(d[i - k] + 1, d[i])

if d[m] < 10001:
    print(d[m])
else:
    print(-1)