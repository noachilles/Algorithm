# 이코테 예제 4-1
# (입력)
# (공간의 크기 - NxN, N)
# (여행가의 이동 계획 R, L, U, D)
# (출력)
# 여행가의 최종 좌표

## 1
n = int(input())
plans = input().split()

x, y = 1, 1
nx, ny = 1, 1

for p in range(len(plans)):
    if plans[p] == 'R':
        nx = x + 1
    elif plans[p] == 'L':
        nx = x - 1
    elif plans[p] == 'U':
        ny = y - 1
    elif plans[p] == 'D':
        ny = y + 1
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    # print(y, x)
print(x, y)


## 2
# n = int(input())
# x, y = 1, 1
# nx, ny = 0, 0
# plans = input().split()

# # L R U D
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
# print(x, y)