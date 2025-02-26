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
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
temp = [[0] * m for _ in range(n)]
result = cnt = 0
v = []

for i in range(n):
    data = list(input().rstrip().split())
    for x in data:
        graph[i].append(int(x))
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
        elif graph[i][j] == 2:
            v.append((i, j))

# virus가 퍼진다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def virus(x, y, temp):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny, temp)
    return

def get_score(temp): # 안전영역의 개수를 구한다
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def make_wall(): # 벽을 만든다
    global cnt
    global result
    cnt_temp = cnt - 3
    for i in range(0, n*m):
        for j in range(i+1, n*m):
            for k in range(j+1, n*m):
                x1 = i // m
                y1 = i % m
                
                x2 = j // m
                y2 = j % m
                
                x3 = k // m
                y3 = k % m
                
                if graph[x1][y1] == 0 and graph[x2][y2] == 0 and graph[x3][y3] == 0:
                    
                    temp = copy.deepcopy(graph)
                    temp[x1][y1] = 1
                    temp[x2][y2] = 1
                    temp[x3][y3] = 1
                    
                    for dot in v:
                        virus(dot[0], dot[1], temp)
                    result = max(result, get_score(temp))
    return result
                
print(make_wall())