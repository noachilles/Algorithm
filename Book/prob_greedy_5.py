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

# 해설
# 문제를 잘못 이해한 것 같다. (예시 꼼꼼하게 확인하기)
# 모든 '조합'을 구하는 것이기 때문에 (1, 4)와 (4, 1)을 함께 카운트하지 않는다.

array = [0] * 11 # 1~10까지 무게를 담을 수 있는 리스트
for x in data:
    # 각 무게에 해당하는 볼링공 개수 카운트
    array[x] += 1
    
result = 0
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외 - 이전 기록과 겹치지 않도록
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)