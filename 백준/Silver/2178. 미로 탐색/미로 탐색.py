from collections import deque
n, m = map(int, input().split())
maze = [] 
# 최소 칸 수
res = [[0] * m for _ in range(n)]
for _ in range(n):
    data = list(map(int, input()))
    maze.append(data)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    res[0][0] = 1
    while q:
        x, y = q.popleft()
        maze[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    if res[nx][ny] > 0:
                        res[nx][ny] = min(res[nx][ny], res[x][y] + 1)
                    else:
                        res[nx][ny] = res[x][y] + 1
                    q.append((nx, ny))
                    maze[nx][ny] = 0
                    
bfs()
print(res[n-1][m-1])
