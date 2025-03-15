from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(arr, visited, y, x):
    global n, m
    temp = [[0] * m for _ in range(n)]
    q = deque()
    q.append((y, x))
    # 방문 처리
    while q:
        y, x = q.popleft()
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 0:
                    cnt += 1
                else:
                    if visited[ny][nx] == 0:
                        q.append((ny, nx))
                        visited[ny][nx] = 1
        temp[y][x] = cnt
    for i in range(n):
        for j in range(m):
            if arr[i][j] < temp[i][j]:
                arr[i][j] = 0
            else:
                arr[i][j] -= temp[i][j]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
while True:
    group = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and visited[i][j] == 0:
                bfs(arr, visited, i, j)
                group += 1
    if group > 1:
        break
    elif group == 0:
        cnt = 0
        break
    cnt += 1
print(cnt)