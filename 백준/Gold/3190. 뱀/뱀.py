import sys
from collections import deque
input = sys.stdin.readline

def rotate(now, d): # 전환 후 방향을 return 해줌
    if d == 'L':
        if now == 0:
            return 3
        else:
            return now - 1
    else:
        if now == 3:
            return 0
        else:
            return now + 1

# 입력
n = int(input()) # 보드 크기
board = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input()) # 사과 개수
for _ in range(k):
    # 사과 위치
    r, c = map(int, input().split())
    board[r][c] = 2 # 몸과 구별하기 위해
l = int(input()) # 방향 전환 횟수
rotation = deque()
for _ in range(l):
    x, c = input().split()
    x = int(x)
    rotation.append((x, c))

snake = deque()

time = 0 # 시간

headx = tailx = 1
heady = taily = 1
snake.append((headx, heady))
board[headx][heady] = 1 # 최초 뱀

xd = [0, 1, 0, -1]
yd = [1, 0, -1, 0]
direction = 0
# 현재 방향이 1이면 x += xd[1], y += yd[1]

while True:
    # 회전이 있다면
    if rotation:
        if time >= rotation[0][0]:
            direction = rotate(direction, rotation[0][1])
            rotation.popleft()
    headx += xd[direction]
    heady += yd[direction]
    snake.appendleft((headx, heady))
    
    # 범위 밖으로 나갈 시
    if headx <= 0 or heady <= 0 or headx > n or heady > n:
        print(time + 1)
        break
    # 자신의 몸과 부딪힐 시
    elif board[headx][heady] == 1:
        print(time + 1)
        break
    # 사과를 먹는다면
    elif board[headx][heady] == 2:
        board[headx][heady] -= 1
        # tail은 변하지 않음
    # 이외(일반)
    else:    
        board[headx][heady] = 1
        board[tailx][taily] = 0
        snake.pop()
        tailx = snake[-1][0]
        taily = snake[-1][1]
    time += 1