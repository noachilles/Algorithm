# 이코테 - 실전문제 5-2

# 입력
# (미로 세로 길이 N, 미로 가로 길이 M)
# (미로 정보 - 괴물이 있음0 괴물이 없음 1)
# 출력
# 탈출구(n, m)까지 움직여야하는 최소 칸의 개수

# 한 번에 한 칸씩 이동할 수 있고, 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어 있다.
# 나: (1, 1) 출구: (N, M) 두 칸을 포함한 최소 이동 칸 수

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 1로만 갈 수 있음 BFS로 가장 끝에 있는 노드까지 가면 반환?

# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프 모든 노드 탐색
# (1, 1) 지점에서부터 BFS를 수행해 모든 노드의 값을 거리 정보로 넣으면 됨
# 특정 노드 방문 시 이전 노드의 거리에 1을 더한 값을 리스트에 넣음

# (1, 1) 지점은 1로 고정되어 있고, 가장 가까운 노드를 찾는 것은?

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))