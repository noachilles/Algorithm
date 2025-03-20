def dfs(x, y):
    global temp, cnt, res
    temp += grid[y][x]
    cnt += 1
    # 만약 4개가 된다면 반환
    if cnt == 4:
        res = max(res, temp)
        temp -= grid[y][x]
        cnt -= 1
        return
    rev = grid[y][x]
    grid[y][x] = -1
    # 4가지 방향에 대해 dfs 수행
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] >= 0:
                dfs(nx, ny)
    grid[y][x] = rev
    temp -= grid[y][x]
    cnt -= 1

# ㅏ, ㅓ, ㅗ, ㅜ 예외 처리
# ㅏ일 때
def f(x, y):
    global res, grid
    # 입력으로 받은 x, y에 대해
    for i in range(4):
        temp = 0
        y1, x1 = y + ex[i][0][0], x + ex[i][0][1]
        y2, x2 = y + ex[i][1][0], x + ex[i][1][1]
        y3, x3 = y + ex[i][2][0], x + ex[i][2][1]
        y4, x4 = y + ex[i][3][0], x + ex[i][3][1]
        # 모든 값이 범위 내에 있다면
        if 0 <= y1 < n and 0 <= y2 < n and 0 <= y3 < n and 0 <= y4 < n and 0 <= x1 < m and 0 <= x2 < m and 0 <= x3 < m and 0 <= x4 < m:
            temp += grid[y1][x1]
            temp += grid[y2][x2]
            temp += grid[y3][x3]
            temp += grid[y4][x4]
        res = max(res, temp)
    
if __name__ == "__main__":
    # dfs 위한 방향 배열
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 예외 처리를 위한 배열
    ex = [[(0, 0), (1, 0), (1, 1), (2, 0)],
          [(0, 0), (1, -1), (1, 0), (2, 0)],
          [(0, 0), (1, -1), (1, 0), (1, 1)],
          [(0, 0), (0, 1), (0, 2), (1, 1)]]

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    res = 0
    for i in range(n):
        for j in range(m):
            temp = 0
            cnt = 0
            dfs(j, i)
            f(j, i)        
    print(res)