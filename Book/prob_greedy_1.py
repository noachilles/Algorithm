# 설명
# 모험가 N명에 대해
# 공포도가 X인 모험가는 X명 이상으로 구성한 모험가 그룹에 참여해야 모험할 수 있음
# 여행을 떠날 수 있는 최대 그룹수

# 입력
# N: 모험가의 수
# 각 모험가의 공포도 값(N이하 자연수)

import sys
input = sys.stdin.readline

n = int(input())
scary = list(map(int, input().split()))

scary.sort()

res = 0
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in scary:
    count += 1 # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:
        res += 1
        count = 0
print(res)