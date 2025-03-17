def roll_dice(ver, hor, d):
    # 주사위의 방향 d 에 따라 hor, ver 업데이트
    n_ver = ver
    n_hor = hor
    if d == 0: # 동쪽
        n_hor = ver[3:] + hor[:2]
        n_ver = ver[:1] + hor[:1] + ver[2:3] + hor[2:]

    elif d == 1: # 서쪽
        n_hor = hor[1:] + ver[3:]
        n_ver = ver[:1] + hor[2:] + ver[2:3] + hor[:1]
        
    elif d == 2: # 북쪽
        n_ver = ver[1:] + ver[:1]
        n_hor[1] = n_ver[1]
        
    else:
        n_ver = ver[3:] + ver[:3]
        n_hor[1] = n_ver[1]
    ver = n_ver
    hor = n_hor
    return ver + hor

def chk_map(r, c, d):
    global N, M, grid
    # 주사위 이동
    dlist = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동-서-북-남
    nr = r + dlist[d][0] 
    nc = c + dlist[d][1]

    if 0 <= nr < N and 0 <= nc < M:
        r = nr
        c = nc
        return (r, c)
    return False
        
def copy_map(ver, hor, r, c):
    global grid
    # 지도가 0인 경우 바닥면 복사
    if grid[r][c] == 0:
        grid[r][c] = ver[3]

    # 바닥면에 지도 복사
    else:
        ver[3] = grid[r][c]
        grid[r][c] = 0
    return ver + hor
    
if __name__ == "__main__":
    ver = [0, 0, 0, 0]
    hor = [0, 0, 0]
    N, M, r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    directions = list(map(int, input().split()))
        
    for d in directions:
        chk = chk_map(r, c, d-1)
        if not chk:
            continue
        else:
            r, c = chk    
            temp = roll_dice(ver, hor, d-1)
            ver, hor = temp[:4], temp[4:]
            temp = copy_map(ver, hor, r, c)
            ver, hor = temp[:4], temp[4:]
            print(ver[1])