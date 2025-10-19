
from collections import deque

def can_goto_end(dist_map):
    '''
    :param dist_map: 종료 지점에서부터의 거리 -> 만약 시작지점이 -1이면 return False
    :return:
    '''
    # 메두사의 집에서 공원까지 가는 경로 있는지 확인
    que = deque()
    que.append((er, ec))
    dist_map[er][ec] = 0
    while que:
        r, c = que.popleft()
        for d in range(4):
            nr, nc = r + directions[d][0], c + directions[d][1]
            if 0 <= nr < N and 0 <= nc < N and dist_map[nr][nc] == -1 and grid[nr][nc] == 0:
                dist_map[nr][nc] = dist_map[r][c] + 1
                que.append((nr, nc))
    if dist_map[sr][sc] == -1:
        return False
    return True

# 메두사의 집까지 경로를 구한다
def get_route_to_end(dist_map):
    r, c = sr, sc
    route = []
    while True:
        if r == er and c == ec:
            break
        for d in range(4):
            nr, nc = r + directions[d][0], c + directions[d][1]
            if 0 <= nr < N and 0 <= nc < N and dist_map[nr][nc] != -1 and (dist_map[r][c] > dist_map[nr][nc]):
                route.append((nr, nc))
                r, c = nr, nc
                break
    return route

# 메두사가 route를 따라 이동한다
def move_medusa(route):
    '''
    route: 메두사가 집에서 공원까지 가는 경로 - 집은 포함되지 않는다
    :return:
    '''
    cr, cc = route[0]
    del_lst = []
    for w in warriors:
        if warriors[w] == (cr, cc):
            del_lst.append(w)
    for i in del_lst:
        warriors.pop(i)
    if len(route) <= 1:
        route = []
    else:
        route = route[1:]
    return cr, cc, route



# 메두사가 위를 볼 때 시야
def see_upper():
    # 메두사 현재 위치를 기준으로 (cr, cc)
    # 다음 레벨~
    # 최대 N-1까지 가능
    sight_map = [[0] * N for _ in range(N)]
    for i in range(1, N):
        # nr이 범위 넘어가면 종료
        nr = cr - i
        if nr < 0:
            break
        for j in range(-i, i+1):
            nc = cc + j
            if 0 <= nc < N:
                sight_map[nr][nc] = 1
    # warriors를 고려해야 한다
    # 아래에서부터 고려한다 - r이 큰 순서대로
    rocked_num = 0
    rocked_lst = []
    w_lst = sorted(warriors.items(), key=lambda x: -x[1][0])
    for w in w_lst:
        w_num, wr, wc = w[0], w[1][0], w[1][1]
        if sight_map[wr][wc] == 0:
            continue
        rocked_num += 1
        rocked_lst.append(w_num)
        # c를 비교해서 범위를 저장
        if wc < cc:
            for i in range(1, N):
                nr = wr - i
                if nr < 0:
                    break
                for j in range(-i, 1):
                    nc = wc + j
                    if 0 <= nc < N:
                        sight_map[nr][nc] = 0

        elif wc > cc:
            for i in range(1, N):
                nr = wr - i
                if nr < 0:
                    break
                for j in range(0, i+1):
                    nc = wc + j
                    if 0 <= nc < N:
                        sight_map[nr][nc] = 0

        elif wc == cc:
            for i in range(1, N):
                nr = wr - i
                if nr < 0:
                    break
                sight_map[nr][wc] = 0
    return rocked_num, rocked_lst, sight_map


def see_down():
    sight_map = [[0] * N for _ in range(N)]
    for i in range(1, N):
        # nr이 범위 넘어가면 종료
        nr = cr + i
        if nr >= N:
            break
        for j in range(-i, i + 1):
            nc = cc + j
            if 0 <= nc < N:
                sight_map[nr][nc] = 1

    # warriors를 고려해야 한다
    # 아래에서부터 고려한다 - r이 작은 순서대로
    rocked_num = 0
    rocked_lst = []
    w_lst = sorted(warriors.items(), key=lambda x: x[1][0])
    for w in w_lst:
        w_num, wr, wc = w[0], w[1][0], w[1][1]
        if sight_map[wr][wc] == 0:
            continue
        rocked_num += 1
        rocked_lst.append(w_num)
        # c를 비교해서 범위를 저장
        if wc < cc:
            for i in range(1, N):
                nr = wr + i
                if nr >= N:
                    break
                for j in range(-i, 1):
                    nc = wc + j
                    if 0 <= nc < N:
                        sight_map[nr][nc] = 0

        elif wc > cc:
            for i in range(1, N):
                nr = wr + i
                if nr >= N:
                    break
                for j in range(0, i+1):
                    nc = wc + j
                    if 0 <= nc < N:
                        sight_map[nr][nc] = 0

        elif wc == cc:
            for i in range(1, N):
                nr = wr + i
                if nr >= N:
                    break
                sight_map[nr][wc] = 0
    return rocked_num, rocked_lst, sight_map


def see_left():
    sight_map = [[0] * N for _ in range(N)]
    for i in range(1, N):
        nc = cc - i
        if nc < 0:
            break
        for j in range(-i, i+1):
            nr = cr + j
            if 0 <= nr < N:
                sight_map[nr][nc] = 1

    # warriors를 고려해야 한다
    # 아래에서부터 고려한다 - c가 큰 순서대로
    rocked_num = 0
    rocked_lst = []
    w_lst = sorted(warriors.items(), key=lambda x: -x[1][1])
    for w in w_lst:
        w_num, wr, wc = w[0], w[1][0], w[1][1]
        if sight_map[wr][wc] == 0:
            continue
        rocked_num += 1
        rocked_lst.append(w_num)
        if wr < cr:
            for i in range(1, N):
                nc = wc - i
                if nc < 0:
                    break
                for j in range(-i, 1):
                    nr = wr + j
                    if 0 <= nr < N:
                        sight_map[nr][nc] = 0
        elif wr > cr:
            for i in range(1, N):
                nc = wc - i
                if nc < 0:
                    break
                for j in range(0, i+1):
                    nr = wr + j
                    if 0 <= nr < N:
                        sight_map[nr][nc] = 0

        elif wr == cr:
            for i in range(1, N):
                nc = wc - i
                if nc < 0:
                    break
                sight_map[wr][nc] = 0
    return rocked_num, rocked_lst, sight_map
    # for i in range(N):
    #     print(sight_map[i])

def see_right():
    sight_map = [[0] * N for _ in range(N)]
    for i in range(1, N):
        nc = cc + i
        if nc >= N:
            break
        for j in range(-i, i + 1):
            nr = cr + j
            if 0 <= nr < N:
                sight_map[nr][nc] = 1

    rocked_num = 0
    rocked_lst = []
    # warriors를 고려해야 한다
    # 아래에서부터 고려한다 - c가 작은 순서대로
    w_lst = sorted(warriors.items(), key=lambda x: x[1][1])
    for w in w_lst:
        w_num, wr, wc = w[0], w[1][0], w[1][1]
        if sight_map[wr][wc] == 0:
            continue
        rocked_num += 1
        rocked_lst.append(w_num)
        if wr < cr:
            for i in range(1, N):
                nc = wc + i
                if nc >= N:
                    break
                for j in range(-i, 1):
                    nr = wr + j
                    if 0 <= nr < N:
                        sight_map[nr][nc] = 0
        elif wr > cr:
            for i in range(1, N):
                nc = wc + i
                if nc >= N:
                    break
                for j in range(0, i+1):
                    nr = wr + j
                    if 0 <= nr < N:
                        sight_map[nr][nc] = 0

        elif wr == cr:
            for i in range(1, N):
                nc = wc + i
                if nc >= N:
                    break
                sight_map[wr][nc] = 0
    return rocked_num, rocked_lst, sight_map

def compute_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

import random
T = 1
for test_case in range(1, T+1):
    see_lst = [see_upper, see_down, see_left, see_right]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    # Common Case
    # N, M = 4, 4
    # sr, sc, er, ec = 1, 3, 3, 3
    # warriors = {1:(3, 1), 2:(0, 3), 3:(1, 0), 4:(2, 2)}
    # grid = [[0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 1, 1],
    #         [1, 0, 0, 0]]

    # Real Input
    N, M = map(int, input().split())
    sr, sc, er, ec = map(int, input().split())
    warriors = dict()
    data = list(map(int, input().split()))
    num = 1
    for i in range(0, 2 * M, 2):
        warriors.update({num: (data[i], data[i+1])})
        num += 1
    grid = [list(map(int, input().split())) for _ in range(N)]



    # 메두사의 집에서부터 공원까지 경로가 있나
    dist_map = [[-1] * N for _ in range(N)]
    flag = can_goto_end(dist_map)
    if not flag:
        print('-1')

    else:
        # 0. 메두사의 집에서부터 공원까지의 경로를 구한다
        route = get_route_to_end(dist_map)
        cr, cc = sr, sc

        while True:
            total_moved, rocked_num, total_attacked = 0, 0, 0
            # 1. 메두사가 이동한다
            cr, cc, route = move_medusa(route)
            # 메두사가 공원에 도착했다면
            if cr == er and cc == ec:
                print('0')
                break

            # 2. 상하좌우를 보며 메두사 시야를 결정
            # 돌이 된 전사 번호
            rocked_lst = []
            # 메두사의 시야 지도
            medusa_map = [[0] * N for _ in range(N)]
            for d in range(4):

                res, lst, sight_map = see_lst[d]()
                # 더 클 경우에만
                if res > rocked_num:
                    rocked_num = res
                    rocked_lst = lst[:]
                    medusa_map = [arr[:] for arr in sight_map]

            # 만약 전사가 없다면 아래 과정은 생략한다~
            if len(warriors) >= 1:

                # 3. 전사들의 이동
                # 돌로 변하지 않은 전사들이 움직일 수 있다
                for num in warriors:
                    # 돌로 변했으면 넘어감
                    if num in set(rocked_lst):
                        continue
                    w_moved = False
                    ar, ac = warriors[num]
                    for d in range(4):
                        nr, nc = ar + directions[d][0], ac + directions[d][1]
                        # 메두사의 시야 지도가 필요하다 / 거리가 더 가까워지는 방향으로
                        if 0 <= nr < N and 0 <= nc < N:
                            if medusa_map[nr][nc] == 0 and (compute_dist((cr, cc), (ar, ac)) > compute_dist((cr, cc), (nr, nc))):
                                w_moved = True
                                total_moved += 1
                                ar, ac = nr, nc
                                break
                    if w_moved:
                        for d in range(4):
                            nr, nc = ar + directions[d][0], ac + directions[d][1]
                            # 메두사의 시야 지도가 필요하다
                            if 0 <= nr < N and 0 <= nc < N:
                                if medusa_map[nr][nc] == 0 and (compute_dist((cr, cc), (ar, ac)) > compute_dist((cr, cc), (nr, nc))):
                                    ar, ac = nr, nc
                                    total_moved += 1
                                    ar, ac = nr, nc
                                    break
                    warriors[num] = (ar, ac)

                # 4. 전사들의 공격
                # 메두사와 같은 칸에 도달했다면!
                del_lst = []
                for num in warriors:
                    if warriors[num] == (cr, cc):
                        total_attacked += 1
                        del_lst.append(num)

                for i in del_lst:
                    warriors.pop(i)

            # 이까지 모두 끝내고 나면
            # 출력: total_moved rocked_num total_attacked
            print(total_moved, rocked_num, total_attacked)