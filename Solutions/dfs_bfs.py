# BOJ - Silver - 2468
# DFS로
# import copy
# import sys
# sys.setrecursionlimit(10**9)
# def dfs(x, y, k):
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False
#     if temp[x][y] > k:
#         temp[x][y] = 0  # 0으로 바꿔줘야 한다  
#         dfs(x+1, y, k)
#         dfs(x-1, y, k)
#         dfs(x, y+1, k)
#         dfs(x, y-1, k)
#         return True
#     temp[x][y] = 0
#     return False

# n = int(input())
# graph = []
# res = 0
# for i in range(n):
#     graph.append(list(map(int, input().split())))
    
# for t in range(100):
#     temp = copy.deepcopy(graph)
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if dfs(i, j, t):
#                 cnt += 1
#     if res < cnt:
#         res = cnt
#     if cnt == 0:
#         break
# print(res)

# BOJ - Silver - 2583
# from collections import deque

# def bfs(x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] = 1
#     cnt = 1
#     while queue:
#         qx, qy = queue.popleft()
#         for i in range(4):
#             nx = qx + dx[i]
#             ny = qy + dy[i]
#             if 0 <= nx <= n-1 and 0 <= ny <= m-1 and not graph[nx][ny]:
#                 if graph[nx][ny] == 0:
#                     queue.append((nx, ny))
#                     graph[nx][ny] = 1
#                     cnt += 1
#     return cnt

# m, n, k = map(int, input().split())
# graph = [[0] * m for _ in range(n)]

# for i in range(k):
#     lx, ly, rx, ry = map(int, input().split())
#     for i in range(lx, rx):
#         for j in range(ly, ry):
#             graph[i][m-1-j] = 1

# res = []
# for x in range(n):
#     for y in range(m):
#         if graph[x][y] == 0:
#             cnt = bfs(x, y)
#             if cnt:
#                 res.append(cnt)
# res.sort() # '오름차순 정렬'
# print(len(res))
# for num in res:
#     print(num, end=' ')

# BOJ - Silver - 2644

# def dfs(o1, res):
#     v[o1] = 1
#     d[o1] = res
#     res += 1
#     # print(o1)
#     for key in arr[o1]: # key에 대해
#         if not v[key]: # 방문 기록이 없다면
#             dfs(key, res)
#             v[key] = 1
  
# d = dict()      
# n = int(input())
# arr = [[] for _ in range(n+1)]
# v = [0] * (n+1)
# o1, o2 = map(int, input().split())
# m = int(input())
# for _ in range(m):
#     x, y = map(int, input().split())
#     arr[x].append(y)
#     arr[y].append(x)
    
# dfs(o1, 0)
# if o2 in d:
#     print(d[o2])
# else:
#     print(-1)

# BOJ - Gold - 14502
# 연구소 각 칸에 대해 3개의 1을 만들고 안전영역을 구함
# import sys
# import copy
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[] for _ in range(n)]
# temp = [[0] * m for _ in range(n)]
# result = cnt = 0
# v = []

# for i in range(n):
#     data = list(input().rstrip().split())
#     for x in data:
#         graph[i].append(int(x))
        
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             cnt += 1
#         elif graph[i][j] == 2:
#             v.append((i, j))

# # virus가 퍼진다
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# def virus(x, y, temp):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny, temp)
#     return

# def get_score(temp): # 안전영역의 개수를 구한다
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score

# def make_wall(): # 벽을 만든다
#     global cnt
#     global result
#     cnt_temp = cnt - 3
#     for i in range(0, n*m):
#         for j in range(i+1, n*m):
#             for k in range(j+1, n*m):
#                 x1 = i // m
#                 y1 = i % m
                
#                 x2 = j // m
#                 y2 = j % m
                
#                 x3 = k // m
#                 y3 = k % m
                
#                 if graph[x1][y1] == 0 and graph[x2][y2] == 0 and graph[x3][y3] == 0:
                    
#                     temp = copy.deepcopy(graph)
#                     temp[x1][y1] = 1
#                     temp[x2][y2] = 1
#                     temp[x3][y3] = 1
                    
#                     for dot in v:
#                         virus(dot[0], dot[1], temp)
#                     result = max(result, get_score(temp))
#     return result
                
# print(make_wall())

# BOJ - Gold - 18405
# from collections import deque
# n, k = map(int, input().split())
# # graph 범위가 n+1 * n+1 이므로 x, y 그대로 사용할 수 있음
# graph = [[0] * (n+1) for _ in range(n+1)]
# virus = [[] for _ in range(k+1)]
# for i in range(1, n+1):
#     graph[i] = [0] + (list(map(int, input().split())))

# s, x, y = map(int, input().split())

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] > 0:
#             virus[graph[i][j]].append((i, j))

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# def spread():
#     cnt = 0
#     for v in range(1, k+1):
#         queue = deque(virus[v])
#         for _ in range(len(queue)):
#             x, y = queue.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 1 <= nx <= n and 1 <= ny <= n:
#                     if graph[nx][ny] == 0:
#                         graph[nx][ny] = v
#                         queue.append((nx, ny))
#         virus[v] = list(queue)
#         if queue == 0:
#             cnt += 1
#     if cnt >= k:
#         return True

# for i in range(s):
#     if spread():
#         break
# print(graph[x][y])

# BOJ - Silver - 14888
# n = int(input())
# data = list(map(int, input().split()))
# # +, -, *, // 
# add, sub, mul, div = map(int, input().split())

# max_value = -1e9 - 1
# min_value = 1e9 + 1

# def dfs(i, now):
#     global max_value, min_value, add, sub, mul, div
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         if add > 0:
#             add -= 1
#             dfs(i + 1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / data[i]))
#             div += 1

# dfs(1, data[0])

# print(max_value)
# print(min_value)

# BOJ - Gold - 16234
# from collections import deque
# import sys
# sys.setrecursionlimit(10**9)

# N, L, R = map(int, input().split()) # 땅의 범위, 최소, 최대
# A = [list(map(int, input().split())) for _ in range(N)]
# B = [[0] * N for _ in range(N)]
# V = [[0] * N for _ in range(N)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# def open(a, b): # 문을 여는 작업
#     q = deque()
#     chk = False
#     q.append((a, b))
#     while q:
#         x, y = q.popleft()
#         if V[x][y] == 0:
#             V[x][y] = 1
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if L <= abs(A[x][y] - A[nx][ny]) <= R and V[nx][ny] == 0:
#                         B[x][y] = 1
#                         B[nx][ny] = 1
#                         chk = True
#                         q.append((nx, ny))
#     return chk

# def bfs(a, b): # 인구 계산, 재정의
#     s = 0
#     c = 0
#     q = deque()
#     stack = []
#     q.append((a, b))
#     stack.append((a, b))
#     while q:
#         x, y = q.popleft()
#         if B[x][y] == 1:
#             B[x][y] = 0
#             s += A[x][y]
#             c += 1
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if B[nx][ny] == 1 and V[nx][ny] == 1:
#                         q.append((nx, ny))
#                         stack.append((nx, ny))
#     if c == 0:
#         return 
#     for t in stack:
#         x, y = t
#         A[x][y] = int(s / c)

# res = 0
# while True:
#     end = True # 변화가 없다면 True
#     for i in range(N):
#         for j in range(N):
#             if V[i][j] == 0:
#                 temp = open(i, j)
#                 if temp: # 변화가 있다면 -> False
#                     end = False
#                     bfs(i, j)
#     if end:
#         break
#     V = [[0] * N for _ in range(N)]
#     res += 1
# print(res)

# BOJ - Silver - 2178
# 이런 건 최단 경로로 풀어야하나?

# from collections import deque
# n, m = map(int, input().split())
# maze = [] 
# # 최소 칸 수
# res = [[0] * m for _ in range(n)]
# for _ in range(n):
#     data = list(map(int, input()))
#     maze.append(data)

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# def bfs():
#     q = deque()
#     q.append((0, 0))
#     res[0][0] = 1
#     while q:
#         x, y = q.popleft()
#         maze[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if maze[nx][ny] == 1:
#                     if res[nx][ny] > 0:
#                         res[nx][ny] = min(res[nx][ny], res[x][y] + 1)
#                     else:
#                         res[nx][ny] = res[x][y] + 1
#                     q.append((nx, ny))
#                     maze[nx][ny] = 0
                    
# bfs()
# print(res[n-1][m-1])

# BOJ - Silver - 1697

# 1을 더하거나 / 1을 빼거나 / 2를 곱하거나
# from collections import deque
# n, k = map(int, input().split())
# MAX = 100001
# d = [0] * MAX


# def bfs():
#     q = deque()
#     q.append((n, 0))
#     while q:
#         x, count = q.popleft()
#         # d[x] = count
#         if x == k:
#             return count
#         for next in (x-1, x+1, x*2):
#             if 0 <= next < MAX and d[next] == 0:
#                 q.append((next, count+1))
#                 d[next] = 1
            

# print(bfs())

# BOJ - Silver - 5014
# 총 F층, 스타트링크는 G층, 지금은 S층
# from collections import deque
# F, S, G, U, D = map(int, input().split())

# visited = [0] * (F+1)

# def bfs():
#     global F, S, G, U, D
#     q = deque()
#     q.append((S, 0))
#     while q:
#         x, cnt = q.popleft()
#         if x == G: # 도착하면 return
#             return cnt
#         for next in (x + U, x - D):
#             if 0 < next <= F and visited[next] == 0:
#                 q.append((next, cnt+1))
#                 visited[next] = 1
#     return -1

# res = bfs()
# if res >= 0:
#     print(res)
# else:
#     print("use the stairs")

# BOJ - 2573
# arr = [[0, 0, 0, 0, 0, 0, 0],
#        [0, 2, 4, 5, 3, 0, 0],
#        [0, 3, 0, 2, 5, 2, 0],
#        [0, 7, 6, 2, 4, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0]]

# arr = [[0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 0, 0],
#         [0, 1, 0, 0, 1, 0, 0],
#         [0, 1, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0]]

# from collections import deque

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(arr, visited, y, x):
#     global n, m
#     temp = [[0] * m for _ in range(n)]
#     q = deque()
#     q.append((y, x))
#     # 방문 처리
#     while q:
#         y, x = q.popleft()
#         cnt = 0
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
            
#             if 0 <= ny < n and 0 <= nx < m:
#                 if arr[ny][nx] == 0:
#                     cnt += 1
#                 else:
#                     if visited[ny][nx] == 0:
#                         q.append((ny, nx))
#                         visited[ny][nx] = 1
#         temp[y][x] = cnt
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] < temp[i][j]:
#                 arr[i][j] = 0
#             else:
#                 arr[i][j] -= temp[i][j]

# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# cnt = 0
# while True:
#     group = 0
#     visited = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] > 0 and visited[i][j] == 0:
#                 bfs(arr, visited, i, j)
#                 group += 1
#     if group > 1:
#         break
#     elif group == 0:
#         cnt = 0
#         break
#     cnt += 1
# print(cnt)

# BOJ - 7569
arr1 = [[[-1, -1, 0, 0, 0],
       [-1, -1, 0, 1, 1],
       [0, 0, 0, 1, 1]]]

arr2 = [[[0, -1, 0, 0, 0],
       [-1, -1, 0, 1, 1],
       [0, 0, 0, 1, 1]]]

arr3 = [[[-1, -1, 1, 1, 1],
       [-1, -1, 1, 1, 1],
       [1, 1, 1, 1, 1]]]

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