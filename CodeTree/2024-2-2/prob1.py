# 그래프를 만들어서 4가지 방향으로 연결된 번호들을 미리 build
# 탐색을 할 때 사용하면 된다
# key point: graph build, len(que)만큼 반복

import sys
sys.stdin = open('input.txt', 'r')

INF = int(1e9)

def set_cell_id():
    cnt = 0 # cnt 1부터 시작
    for r in range(N):
        for c in range(N):
            # 시간의 벽이면 넘어간다
            if space[r][c] == 3:
                continue
            cnt += 1
            space_cell_id[r][c] = cnt

    for i in range(5):
        for r in range(M):
            for c in range(M):
                cnt += 1
                wall_cell_id[i][r][c] = cnt

    return cnt

def build_graph():
    '''
    :param cnt:
    :return:
    '''
    # 평면도에서 서로 연결된 접점을 찾는다 - 시간의 벽 범위 제외
    for r in range(N):
        for c in range(N):
            id_now = space_cell_id[r][c]
            for d in range(4):
                nr, nc = r + directions[d][0], c + directions[d][1]
                # 범위 내에 있고 시간의 벽 범위가 아니면
                if 0 <= nr < N and 0 <= nc < N and space[nr][nc] != 3:
                    graph[id_now][d] = space_cell_id[nr][nc]

    # 동서남북 단면도에서 서로 연결된 접점을 찾는다
    for i in range(4):
        for r in range(M):
            for c in range(M):
                id_now = wall_cell_id[i][r][c]
                for d in range(4):
                    nr, nc = r + directions[d][0], c + directions[d][1]
                    # 범위 내에 있다면 그냥 저장
                    if 0 <= nr < M and 0 <= nc < M:
                        graph[id_now][d] = wall_cell_id[i][nr][nc]
                    # 행을 벗어나면 out - 따로 처리
                    if nr < 0 or nr >= M:
                        continue
                    # 열이 0보다 작으면 뒤의 것: (행은 그대로, 열은 M-1) 동->남->서->북
                    if nc < 0:
                        graph[id_now][d] = wall_cell_id[(i + 1) % 4][nr][M-1]
                    # 열이 M보다 크거나 같으면 앞의 것: (행은 그대로, 열은 0)  동<-남<-서<-북
                    if nc >= M:
                        graph[id_now][d] = wall_cell_id[(i - 1) % 4][nr][0]

    # 위쪽 단면도에서 연결된 접점을 찾는다 - 동서남북과 연결은 따로
    for r in range(M):
        for c in range(M):
            id_now = wall_cell_id[4][r][c]
            for d in range(4):
                nr, nc = r + directions[d][0], c + directions[d][1]

                if 0 <= nr < M and 0 <= nc < M:
                    graph[id_now][d] = wall_cell_id[4][nr][nc]

    # 예외처리 1. 윗면과 동서남북
    # wall_cell_id를 기준으로 사용한다
    # 위 - 동
    for i in range(M):
        # 윗면
        id_x = wall_cell_id[4][i][M-1]
        # 동쪽
        id_y = wall_cell_id[0][0][M-1-i]
        graph[id_x][0] = id_y
        graph[id_y][3] = id_x

    # 위 - 남
    for i in range(M):
        # 위
        id_x = wall_cell_id[4][M-1][i]
        # 남
        id_y = wall_cell_id[1][0][i]
        graph[id_x][1] = id_y
        graph[id_y][3] = id_x

    # 위 - 서
    for i in range(M):
        # 위
        id_x = wall_cell_id[4][i][0]
        id_y = wall_cell_id[2][0][i]
        graph[id_x][2] = id_y
        graph[id_y][3] = id_x

    # 위 - 북
    for i in range(M):
        id_x = wall_cell_id[4][0][i]
        id_y = wall_cell_id[3][0][M-1-i]
        graph[id_x][3] = id_y
        graph[id_y][3] = id_x

    # 예외처리 2. 시간의 벽과 미지의 공간 바닥
    # 미지의 공간에서 시간의 벽 시작 위치를 찾는다
    sr, sc = -1, -1
    for r in range(N):
        for c in range(N):
            if space[r][c] == 3:
                sr, sc = r, c
                break
        if sr != -1:
            break

    # sr, sc를 이용해서 연결한다
    # 모든 벽면에서는 남쪽을 향함 -> graph[idx][1] = idy 고정
    # 동쪽과 바닥
    if sc + M < N:
        for i in range(M):
            idx = wall_cell_id[0][M-1][i]
            idy = space_cell_id[sr + M - i - 1][sc + M]

            graph[idx][1] = idy
            graph[idy][2] = idx

    # 남쪽과 바닥
    if sr + M < N:
        for i in range(M):
            idx = wall_cell_id[1][M-1][i]
            idy = space_cell_id[sr + M][sc + i]
            graph[idx][1] = idy
            graph[idy][3] = idx

    # 서쪽과 바닥
    if sc - 1 >= 0:
        for i in range(M):
            idx = wall_cell_id[2][M-1][i]
            idy = space_cell_id[sr + i][sc - 1]
            graph[idx][1] = idy
            graph[idy][0] = idx

    # 북쪽과 바닥
    if sr - 1 >= 0:
        for i in range(M):
            idx = wall_cell_id[3][M-1][i]
            idy = space_cell_id[sr - 1][sc + M - i - 1]
            graph[idx][1] = idy
            graph[idy][1] = idx

def spread(runs):
    for i in range(F):
        r, c, d, v, alive = phenomenons[i]
        if not alive:
            continue
        if runs % v:
            continue
        # 동쪽
        if d == 0:
            nr = r
            nc = c + 1
        # 서쪽
        elif d == 1:
            nr = r
            nc = c - 1
        # 남쪽
        elif d == 2:
            nr = r + 1
            nc = c
        # 북쪽
        elif d == 3:
            nr = r - 1
            nc = c

        # 장애물이 있으면 움직이지 않는다
        if not (0 <= nr < N and 0 <= nc < N):
            phenomenons[i] = (r, c, d, v, 0)
            continue
        if space[nr][nc]:
            phenomenons[i] = (r, c, d, v, 0)
            continue
        dist[space_cell_id[nr][nc]] = INF
        phenomenons[i] = (nr, nc, d, v, 1)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북
T = 1
for test_case in range(1, T+1):
    N, M, F = map(int, input().split())
    # 처음 입력되는 평면도 저장
    space = [list(map(int, input().split())) for _ in range(N)]
    # 그래프 번호를 담을 셀 저장
    space_cell_id = [[-1] * N for _ in range(N)]
    # 입력되는 평면도 저장
    wall = [[[0] * M for _ in range(M)] for _ in range(5)]
    # 편의상 동 0, 남 1, 서 2, 북 3, 위 4 순으로 받음
    wall[0] = [list(map(int, input().split())) for _ in range(M)]
    wall[2] = [list(map(int, input().split())) for _ in range(M)]
    wall[1] = [list(map(int, input().split())) for _ in range(M)]
    wall[3] = [list(map(int, input().split())) for _ in range(M)]
    wall[4] = [list(map(int, input().split())) for _ in range(M)]
    # 시간의 벽의 그래프 번호를 담을 셀 저장
    wall_cell_id = [[[-1] * M for _ in range(M)] for _ in range(5)]

    phenomenons = dict()
    for i in range(F):
        r, c, d, v = map(int, input().split())
        alive = 1
        phenomenons.update({i: (r, c, d, v, alive)})

    # 입력 끝

    # cell_id 모두 초기화 해줌
    cnt = set_cell_id()

    # 서로 연결을 위해서 graph를 사용한다 - 서로 연결된 접점을 찾기 위해서
    graph = [[-1] * 4 for _ in range(cnt+1)]
    build_graph()

    # 초기 위치 반영
    # 머신 초기 위치 찾기
    machine = -1
    for r in range(M):
        for c in range(M):
            if wall[2][r][c] == 2:
                machine = wall_cell_id[2][r][c]
                break
        if machine != -1:
            break

    # 탈출구 위치 찾기
    end_p = -1
    for r in range(N):
        for c in range(N):
            if space[r][c] == 4:
                end_p = space[r][c]
                break
        if end_p != -1:
            break

    dist = [-1 for _ in range(cnt+1)]

    # 갈 수 없는 곳 dist에서 INF 표시
    # 1. 장애물이 있는 곳
    for r in range(N):
        for c in range(N):
            if space[r][c] == 1:
                dist[space_cell_id[r][c]] = INF

    for i in range(5):
        for r in range(M):
            for c in range(M):
                if wall[i][r][c] == 1:
                    dist[wall_cell_id[i][r][c]] = INF

    for i in range(F):
        r, c, v, d, alive = phenomenons[i]
        dist[space_cell_id[r][c]] = INF

    from collections import deque
    que = deque()
    que.append(machine)
    # start_point의 dist를 0으로 만듦
    dist[machine] = 0

    runs = 1
    while True:
        # 이상현상 확산
        spread(runs)
        # 이상현상이 확산된 위치 반영

        # 셀에 영향을 미치는지 확인

        # 반영해서 이번 턴에 갈 수 있는 셀을 확인
        next_cells = []
        size = len(que)
        for _ in range(size):
            id_now = que.popleft()
            for d in range(4):
                id_nxt = graph[id_now][d]
                # 범위 바깥
                if id_nxt == -1:
                    continue
                # 이미 방문했다면
                if dist[id_nxt] != -1:
                    continue
                dist[id_nxt] = runs
                next_cells.append(id_nxt)

        # 만약 더 이상 도달 가능한 곳이 없다면
        if not next_cells:
            break
        que.extend(next_cells)
        # 만약 end값에 이미 도착했다면
        if dist[end_p] != -1:
            break
        runs += 1

    # 도달했는지 확인
    if dist[end_p] == -1 or dist[end_p] >= INF:
        print(-1)
    else:
        print(dist[end_p])