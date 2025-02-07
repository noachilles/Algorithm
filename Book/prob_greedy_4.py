# 설명
# N개의 동전을 이용해 만들 수 없는 양의 정수 금액 중 최솟값
# N = 5, 각 동전이 3, 2, 1, 9원이라면 res: 8원
# N = 3, 각 동전이 3, 5, 7원이면 res: 1원

# 입력
# N: 동전의 개수
# N개의 자연수: 동전의 단위
import sys
input = sys.stdin.readline
MAX = 1000000

n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)

res = 0

for target in range(1, MAX):
    res = target
    for c in coin:
        # target == 0이 만족된다면: OK
        # target >= c를 만족하는 c가 존재하는지 먼저 살피기
            # target >= c가 만족되는 것이 하나도 없다면 -> 종료
        # target >= c를 만족한는 것이 하나라도 있다면 -> 빼고 continue
        if target == 0:
            break
        elif target >= c:
            target -= c
        else: 
            continue # 다음 c에 대해 동일작업 반복
    if target > 0:
        print(res)
        break
    
# 그리디 문제를 좀 더 많이 접해보자
# 그리디: 현재 상태에서 매번 가장 좋아보이는 것만을 선택하는 알고리즘
# 현재 확인하는 화폐의 단위가 target 이하여야 target을 만들 수 있음
# 따라서 target보다 큰 화폐가 등장하면 해당 target값은 만들 수 없는 값임(1~target-1의 범위 값은 만들 수 있음)
coin.sort()

target = 1
for x in coin:
    if target < x:
        break
    target += x

print(target)