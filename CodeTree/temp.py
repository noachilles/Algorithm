from collections import deque


# 레이저로 공격할 수 있는지 확인
def make_laser_map():
    '''
    attacker: 공격자 (r, c)
    defense: 공격대상 (r, c)
    grid: 0이 아니어야 지나갈 수 있음
    '''
    laser_map = [[-1] * M for _ in range(N)]
    er, ec = defense
    que = deque()
    que.append((er, ec, 0))
    laser_map[er][ec] = 0
    while que:
        r, c, dist = que.popleft()
        # 역순이므로 순서 반대
        for d in range(3, -1, -1):
            nr, nc = (r + directions[d][0]) % N, (c + directions[d][1]) % M
            if laser_map[nr][nc] == -1 and grid[nr][nc] != 0:
                laser_map[nr][nc] = dist + 1
                que.append((nr, nc, dist + 1))
    return laser_map


def laser_attack():
    '''
    laser_map: 레이저 최단 경로 담긴 지도
    grid: 포탑 공격력 담긴 지도
    del_lst: 공격을 통해 부서지는 포탑 (r, c) 담을 리스트
    attacker: 공격자의 (r, c)
    defense: 수비자의 (r, c)
    '''
    r, c = attacker
    whole_power = grid[r][c]
    half_power = grid[r][c] // 2
    # 레이저 경유 포탑 리스트
    end = False
    while not end:
        for d in range(4):
            nr, nc = (r + directions[d][0]) % N, (c + directions[d][1]) % M
            # 작아지는 방향으로만 이동
            if laser_map[nr][nc] != -1 and laser_map[r][c] > laser_map[nr][nc]:
                damaged_lst.append((nr, nc))
                # 만약 nr, nc가 er, ec가 아니라면
                if (nr, nc) != defense:
                    if grid[nr][nc] <= half_power:
                        del_lst.append((nr, nc))
                        grid[nr][nc] = 0
                    else:
                        grid[nr][nc] -= half_power
                        alive[(nr, nc)] = (alive[(nr, nc)][0] - half_power, alive[(nr, nc)][1])
                    r, c = nr, nc
                    break
                else:
                    if grid[nr][nc] <= whole_power:
                        del_lst.append((nr, nc))
                        grid[nr][nc] = 0
                    else:
                        grid[nr][nc] -= whole_power
                        alive[(nr, nc)] = (alive[(nr, nc)][0] - whole_power, alive[(nr, nc)][1])
                    end = True
                    break


def boom_attack():
    '''
    defense 좌표와 인접한 8칸에 대해서
    '''
    sr, sc = attacker
    whole_power = grid[sr][sc]
    half_power = whole_power // 2

    er, ec = defense
    damaged_lst.append(defense)

    # 공격자는 해당 공격의 영향을 받지 않는다 -> 깜빡한 조건

    for d in range(8):
        nr, nc = (er + directions[d][0]) % N, (ec + directions[d][1]) % M
        if (nr, nc) == attacker:
            continue
        if grid[nr][nc] != 0:
            # 포탑 보강을 위해 append
            damaged_lst.append((nr, nc))
            if grid[nr][nc] <= half_power:
                del_lst.append((nr, nc))
                grid[nr][nc] = 0
            else:
                grid[nr][nc] -= half_power
                alive[(nr, nc)] = (alive[(nr, nc)][0] - half_power, alive[(nr, nc)][1])
    if grid[er][ec] <= whole_power:
        del_lst.append((er, ec))
        grid[er][ec] = 0
    else:
        grid[er][ec] -= whole_power
        alive[(er, ec)] = (alive[(er, ec)][0] - whole_power, alive[(er, ec)][1])


T = 1
for test_case in range(1, T + 1):

    # 우 하 좌 상 좌상대 우상대 우하대 좌하대
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    # Common Case
    # N, M, K = 4, 4, 2
    # grid = [[0, 30, 4, 4],
    #         [30, 30, 1, 1],
    #         [8, 0, 1, 26],
    #         [0, 1, 0, 0]]

    # Edge Case
    # N, M, K = 10, 10, 1000
    # grid = []
    # for r in range(N):
    #     data = []
    #     for c in range(M):
    #         data.append(random.randrange(0, 5000))
    #     grid.append(data)

    # Real Input
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # grid 중에서 (r, c)가 0인 경우를 추가
    broken = []
    alive = dict()  # (r, c): (grid[r][c], 공격 turn)
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                broken.append((r, c))
            else:
                alive.update({(r, c): (grid[r][c], 0)})

    for k in range(1, K + 1):

        # 1. 공격자 선정
        sorted_alive = sorted(alive.items(), key=lambda x: (x[1][0], -x[1][1], -(x[0][0] + x[0][1]), -x[0][1]))
        # 공격자: attacker / 수비자: defense
        attacker = sorted_alive[0][0]  # (r, c)를 저장
        # 공격자에게 패널티를 주고 변경
        grid[attacker[0]][attacker[1]] += (N + M)
        alive[attacker] = (alive[attacker][0] + (N + M), k)
        # 공격 대상 선정
        defense = sorted_alive[-1][0]

        # 2. 공격
        # 공격 여부
        attacked = False
        del_lst = []
        damaged_lst = []
        # (1) 레이저 공격
        # 레이저로 공격할 수 있는지 확인한다
        laser_map = make_laser_map()
        # 레이저로 공격할 수 있다면
        if laser_map[attacker[0]][attacker[1]] != -1:
            # 공격
            laser_attack()
            attacked = True

        # (2) 포탄 공격
        if not attacked:
            boom_attack()

        # 3. 포탑 부서짐
        for i in del_lst:
            alive.pop(i)
            broken.append(i)

        # 여기서 포탑 개수 확인
        if len(alive) == 1:
            break

        # 4. 포탑 정비
        for x in alive:
            if x in set(damaged_lst):
                continue
            if x == attacker:
                continue
            if x == defense:
                continue
            alive[x] = (alive[x][0] + 1, alive[x][1])
            grid[x[0]][x[1]] += 1

    result = sorted(alive.values())
    print(result[-1][0])
