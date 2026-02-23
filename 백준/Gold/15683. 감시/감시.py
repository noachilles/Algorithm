# CCTV의 개수대로 중복 조합을 수행한다
# CCTV의 개수만큼 (0, 1, 2, 3)의 값 중 하나씩을 갖도록
def h(k, new, start):
    global cctv_lst
    if len(new) == k:
        # print(new)
        # 각 CCTV의 방향에 대해 감시한다
        watch(new)
        return
    for i in range(start, 4):
        h(k, new + [i], start)
        
        
# 각 CCTV 방향에 대해 감시한다
def watch(new):
    global zero, mn
    temp = 0
    chk_lst = []
    for i in range(len(new)):
        # cctv 번호와 방향
        c, x, y = cctv_lst[i]
        d = new[i]
        # c와 d에 맞게 감시하고.. 해당 좌표를 chk_lst에 넣는다
        # 벽에 부딪힐 때까지 해야하므로 while 반복 & 종료조건 걸어줌
        if c == 1:
            f(chk_lst, d, x, y)
            
        elif c == 2: 
            f(chk_lst, d, x, y)
            f(chk_lst, (d+2) % 4, x, y)
        
        elif c == 3:
            f(chk_lst, d, x, y)
            f(chk_lst, (d+1) % 4, x, y)
            
        elif c == 4:
            f(chk_lst, d, x, y)
            f(chk_lst, (d-1) % 4, x, y)
            f(chk_lst, (d+1) % 4, x, y)
            
        else: 
            f(chk_lst, 0, x, y)
            f(chk_lst, 1, x, y)
            f(chk_lst, 2, x, y)
            f(chk_lst, 3, x, y)
            
        temp = len(set(chk_lst))
        mn = min(mn, zero - temp)
        
# 아래 부분을 함수로 만들어서 1, 2, 3, 4 모두 반복 수행하면 될 것 같음
def f(chk_lst, d, x, y):
    global grid, M, N
    while True:       
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if not (0 <= nx < M and 0 <= ny < N):
            return
        if grid[ny][nx] == 6:
            return
        # 종료되지 않는 한
        if grid[ny][nx] == 0:
            chk_lst.append((nx, ny))    
        x, y = nx, ny

if __name__ == "__main__":
    
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    cctv_lst = []
    zero = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 0:
                zero += 1
            elif grid[y][x] < 6:
                cctv_lst.append((grid[y][x], x, y))
    
    mn = zero
    h(len(cctv_lst), [], 0)
    print(mn)