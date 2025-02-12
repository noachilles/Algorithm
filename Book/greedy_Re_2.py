# 설명
# 뽑고자 하는 카드 포함된 행 선택
# 선택된 행에 포함된 카드 중 숫자가 낮은 카드 선택

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

res = 0

for array in board:
    array.sort()
    if res < array[0]:
        res = array[0]
print(res)