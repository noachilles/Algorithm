from collections import deque

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


# 덜익은 토마토 개수 세기
def cnt_except_green(grid):
    global m, n, h
    cnt = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if grid[z][y][x] == 1 or grid[z][y][x] == -1:
                    cnt += 1
    return cnt

# bfs
def bfs(grid, visited, start):
    global m, n, h
    t_green = 0
    q = deque(start)
    not_yet = []
    while q:
        cz, cy, cx = q.popleft()
        visited[cz][cy][cx] = 1
        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if grid[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                    not_yet.append((nz, ny, nx))
                    visited[nz][ny][nx] = 1
    return not_yet


if __name__ == "__main__":
    m, n, h = map(int, input().split())
    grid = [list(list(map(int, input().split())) for j in range(n)) for i in range(h)]
    
    # 모두 익은 토마토면 0 출력
    ngreen = cnt_except_green(grid)
    if ngreen == m * n * h:
        print(0)
        exit()
    
    visited = [[[0] * m for i in range(n)] for j in range(h)]

    day = 0

    start = []
    
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if grid[z][y][x] == 1 and not visited[z][y][x]:
                    # 익는 토마토의 좌표가 반환된다
                    start.append((z, y, x))
    while True:
        start = bfs(grid, visited, start)
        # 더 이상 변화가 없으면 익지 않은 토마토 개수를 세면 된다   
        if not start:
            break
        ngreen += len(start)
        day += 1
    if ngreen == m * n * h:
        print(day)
    else:
        print(-1)