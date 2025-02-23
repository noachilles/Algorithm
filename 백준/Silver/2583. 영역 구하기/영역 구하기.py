from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    cnt = 1
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and not graph[nx][ny]:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = 1
                    cnt += 1
    return cnt

m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            graph[i][m-1-j] = 1

res = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            cnt = bfs(x, y)
            if cnt:
                res.append(cnt)
res.sort() # '오름차순 정렬'
print(len(res))
for num in res:
    print(num, end=' ')