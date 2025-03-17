dlist = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향 북-동-남-서 0, 1, 2, 3

def f(grid, r, c, d):
    cnt = 0
    while True:
        # 현재 칸이 청소되지 않은 칸
        if grid[r][c] == 0:
            # 청소 후 개수 세기, 청소되면 -1로 변경
            cnt += 1
            grid[r][c] = -1
            
        # 빈 칸 여부 판단
        chk = False
        for i in range(4):
            dr, dc = r + dlist[i][0], c + dlist[i][1]
            if grid[dr][dc] == 0:
                chk = True
                
        # 주위에 빈 칸이 있다면
        if chk == True:
            # 반시계 90도 회전
            if d != 0:
                d -= 1
            else:
                d = 3
            nr, nc = r + dlist[d][0], c + dlist[d][1]
            if grid[nr][nc] == 0:
                r, c = nr, nc
            continue
        
        # 빈 칸이 없다면
        if not chk:
            # 방향 유지한 채 후진
            nr, nc = r - dlist[d][0], c - dlist[d][1]
            if grid[nr][nc] == 1:
                return cnt
            else:
                r, c = nr, nc
                continue
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(f(grid, r, c, d))