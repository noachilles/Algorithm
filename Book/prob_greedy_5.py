# 설명
# 볼링공 N개, 번호는 1번부터 순서대로 부여(1 ~ N+1)
# 같은 무게 공도 서로 다른 공으로 간주, 볼링공 무게는 (1 ~ M)
# A, B가 서로 다른 무게의 공을 선택하는 경우의 수

# 입력
# N, M
# 각 볼링공 무게
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
res = 0

for i in range(n):
    for j in range(i + 1, n):
        if data[i] != data[j]:
            res += 1
print(res)