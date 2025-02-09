# 설명
# NxN 정사각 보드 위에서
# 사과를 먹으면 뱀 길이 + / 벽 or 자기자신과 부딪히면 end
# 게임 시작 시 뱀은 맨 위 맨 좌측, 길이는 1 -> 처음엔 오른쪽 향함

# 조건
# 매 초마다 이동하며
# 몸길이를 늘려 -> 머리를 다음칸에 위치시킴
# 벽이나 자기자신의 몸과 부딪히면 게임 끝
# 이동한 칸에 사과 있으면 사과 없어지고, 꼬리는 움직이지 않음(머리는 이동)
# 이동한 칸에 사과 없을 시 머리 이동 후 꼬리 칸을 비워줌

# 입력
# 보드의 크기 N(2<= N <= 100)
# 사과의 개수 K(0 <= K <= 100)
# K줄 ~ 사과의 위치: 행 열 (1, 1에는 사과 X)
# 방향 변환 횟수 L
# L줄 ~ 방향 변환 정보: 정수 X, 문자 C - 시작 이후 X초가 '끝난' 뒤 왼쪽('L'), 오른쪽('D')으로 90도 회전

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