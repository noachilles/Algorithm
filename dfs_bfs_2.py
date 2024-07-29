# 이코테 - 실전문제 5-2

# 입력
# (미로 세로 길이 N, 미로 가로 길이 M)
# (미로 정보 - 괴물이 있음0 괴물이 없음 1)
# 출력
# 탈출구(n, m)까지 움직여야하는 최소 칸의 개수

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 0
    p = (0, 0)
    
    while queue:
        x, y = queue.popleft()
        # graph[x][y] = 0
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        if nx == (n-1) and ny == (m-1):
            break
    return graph[n-1][m-1]

print(bfs(0, 0))