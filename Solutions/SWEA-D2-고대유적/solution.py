"""
땅속의 구조물을 촬영할 수 있음
폭 1m, 길이 2m 이상의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있음
구조물이 있으면 1, 없으면 0

가장 긴 구조물의 길이 찾기
"""

# 모든 칸을 방문하면서 - 방문 여부를 살피는데, 서로 겹치는 칸일 수 있으니까
# 방향 정보를 함께 저장해줘야 한다
# 1칸, 2칸, 3칸, ..., 다음 칸이 0이라면 현재까지의 길이를 저장하고, 최대 길이와 비교한다

import sys
sys.stdin = open("input.in", "r")

directions = [(1, 0), (0, 1)]   # 아래로 1칸, 오른쪽으로 1칸

def f(r, c, d, l):
    '''
    r: 행
    c: 열
    d: 방향 - 0: 세로 / 1: 가로
    '''
    global res
    # 다음 방향으로 가야함
    # 만약 다음 칸이 0이라면, 현재 값으로 비교해야 함
    # 1부터 시작해야 함
    nr, nc = r + directions[d][0], c + directions[d][1]
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
        if l > res:
            res = l
        return
    if grid[nr][nc] == 0:
        # 현재 길이가 l이라고 할 때, l과 비교해야 함
        if l > res:
            res = l
        return
    # 0이 아닌 상황이라면,
    if (nr, nc, d) not in visited:
        visited.add((nr, nc, d))
        f(nr, nc, d, l+1)

T = int(input())
for tc in range(1, T+1):
    res = 1
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 방문 기록
    visited = set()

    for r in range(N):
        for c in range(M):
            # 방향 세로, 가로
            # 값이 1이면서, 방문 기록이 없으면 그 때 조회를 시도함
            for d in range(2):
                if grid[r][c] == 1 and (r, c, d) not in visited:
                    # 계속 이어지는 블록을 찾고, 로직을 수행하는 함수
                    visited.add((r, c, d))
                    f(r, c, d, 1)
    print(f'#{tc} {res}')