import sys
sys.stdin.readline

def dfs(i, j):
    stack = []
    chk = False
    stack.append((i, j))
    while stack:
        x, y = stack.pop()
        if ground[x][y] == 1:
            chk = True
            for d in range(4):
                if x+dx[d] <= -1 or x+dx[d] >= m or y+dy[d] <= -1 or y+dy[d] >= n:
                    continue
                else:
                    if ground[x+dx[d]][y+dy[d]] == 1:
                        stack.append((x+dx[d], y+dy[d]))
                ground[x][y] = 0
    return chk

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

t = int(input())
while t > 0:
    m, n, k = map(int, input().split())
    ground = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    print(cnt)
    t -= 1