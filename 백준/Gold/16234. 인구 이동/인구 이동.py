from collections import deque
import sys
sys.setrecursionlimit(10**9)

N, L, R = map(int, input().split()) # 땅의 범위, 최소, 최대
A = [list(map(int, input().split())) for _ in range(N)]
B = [[0] * N for _ in range(N)]
V = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def open(a, b): # 문을 여는 작업
    q = deque()
    chk = False
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if V[x][y] == 0:
            V[x][y] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(A[x][y] - A[nx][ny]) <= R and V[nx][ny] == 0:
                        B[x][y] = 1
                        B[nx][ny] = 1
                        chk = True
                        q.append((nx, ny))
    return chk

def bfs(a, b): # 인구 계산, 재정의
    s = 0
    c = 0
    q = deque()
    stack = []
    q.append((a, b))
    stack.append((a, b))
    while q:
        x, y = q.popleft()
        if B[x][y] == 1:
            B[x][y] = 0
            s += A[x][y]
            c += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if B[nx][ny] == 1 and V[nx][ny] == 1:
                        q.append((nx, ny))
                        stack.append((nx, ny))
    if c == 0:
        return 
    for t in stack:
        x, y = t
        A[x][y] = int(s / c)

res = 0
while True:
    end = True # 변화가 없다면 True
    for i in range(N):
        for j in range(N):
            if V[i][j] == 0:
                temp = open(i, j)
                if temp: # 변화가 있다면 -> False
                    end = False
                    bfs(i, j)
    if end:
        break
    V = [[0] * N for _ in range(N)]
    res += 1
print(res)