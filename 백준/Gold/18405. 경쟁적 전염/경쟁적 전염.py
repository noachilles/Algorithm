from collections import deque
n, k = map(int, input().split())
# graph 범위가 n+1 * n+1 이므로 x, y 그대로 사용할 수 있음
graph = [[0] * (n+1) for _ in range(n+1)]
virus = [[] for _ in range(k+1)]
for i in range(1, n+1):
    graph[i] = [0] + (list(map(int, input().split())))

s, x, y = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] > 0:
            virus[graph[i][j]].append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def spread():
    cnt = 0
    for v in range(1, k+1):
        queue = deque(virus[v])
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = v
                        queue.append((nx, ny))
        virus[v] = list(queue)
        if queue == 0:
            cnt += 1
    if cnt >= k:
        return True

for i in range(s):
    if spread():
        break
print(graph[x][y])