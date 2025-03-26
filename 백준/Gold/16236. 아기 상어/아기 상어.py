from collections import deque    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(y, x, shark):
    global eat_lst
    visited = [[0] * N for _ in range(N)]
    que = deque()
    que.append((0, x, y))
    visited[y][x] = 1
    # 종료를 위한 조건
    end = float('inf')
    while que:
        dist, cx, cy = que.popleft()
        if dist == end:
            return
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 방문한 적 없고 물고기의 크기가 상어보다 작으면 queue에 추가
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and ocean[ny][nx] <= shark:
                que.append((dist+1, nx, ny))
                visited[ny][nx] = 1
                # 만약 먹을 수 있는 물고기가 있다면
                if 0 < ocean[ny][nx] < shark:
                    end = dist + 1
                    eat_lst.append((dist+1, nx, ny))

N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]
# 최초
sr, sc = 0, 0
for r in range(N):
    for c in range(N):
        if ocean[r][c] == 9:
            sr, sc = r, c
            break

time = 0 # 시간
shark = 2
cnt = 0
while True:
    eat_lst = []
    bfs(sr, sc, shark)
    # 먼저 먹을 물고기 정렬
    eat_lst = sorted(eat_lst, key=lambda x:(x[2], x[1]))
    if eat_lst:
        ocean[sr][sc] = 0
        t, x, y = eat_lst[0]
        sr, sc = y, x
        ocean[y][x] = 0
        cnt += 1
        time += t
        if cnt >= shark:
            shark += 1
            cnt = 0
    else:
        break
print(time)