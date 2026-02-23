from collections import deque

# 조합
def combinations(m, arr, start):
    global mn, zero
    if len(arr) == m:
        mn = min(mn, bfs(arr, zero))
        return
    for i in range(start, len(virus)):
        combinations(m, arr + [virus[i]], i+1)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(arr, zero):
    visited = [[0] * N for _ in range(N)]
    time = 0
    que = deque()
    for i in range(M):
        y, x = arr[i]
        que.append((0, y, x))
        visited[y][x] = 1
    while que:
        dist, y, x = que.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and grid[ny][nx] != 1: 
                if grid[ny][nx] == 0:
                    time = dist+1
                    zero -= 1
                visited[ny][nx] = dist+1
                que.append((dist+1, ny, nx))
    if zero == 0:
        return time
    else:
        return float('inf')

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
mn = float('inf')
zero = 0
# 바이러스 위치를 저장        
virus = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus.append((i, j))
        if grid[i][j] == 0:
            zero += 1
# 바이러스를 선택한다
combinations(M, [], 0)
if mn == float('inf'):
    print(-1)
else:
    print(mn)