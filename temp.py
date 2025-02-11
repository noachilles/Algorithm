# 백준 - Silver - 1427

# 수의 각 자리수를 내림차순 정렬
# 기수정렬

# n = int(input())
# array = [0] * 10

# k = 10
# while n > 0:
#     v = n % k
#     n //= k
#     array[v] += 1

# for i in range(len(array)-1, -1, -1):
#     while array[i] > 0:
#         print(i, end='')
#         array[i] -= 1
    
# 백준 - Bronze - 2798

# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# res = sum = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             sum += array[i]
#             sum += array[j]
#             sum += array[k]
#             if sum <= m:
#                 res = max(res, sum)
#             sum = 0
# print(res)

# 백준 - Silver - 11650

# n = int(input())
# array = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     array.append((x, y))

# array = sorted(array, key=lambda x : (x[0], x[1]))
# for t in array:
#     print(t[0], t[1], end="\n")

# 백준 - Silver - 11651

# n = int(input())
# array = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     array.append((x, y))

# array = sorted(array, key=lambda x : (x[1], x[0]))
# for t in array:
#     print(t[0], t[1], end="\n")

# 백준 - Silver - 10814

# n = int(input())
# d = dict()
# for i in range(n):
#     age, name = map(str, input().split())
#     d[i] = (age, name)
    
# d = sorted(d.items(), key=lambda x: (x[1][0], x[0]))
# for v in d:
#     print(v[1][0], v[1][1], end='\n')

# 백준 - Silver - 10815

# array: 가지고 있는 숫자 카드
# target: 가지고 있는지 아닌지

# 방법 1. 
# 교집합을 찾아서 -> 그 원소가 있는 위치를 찾아<< index 함수로, res[i] 값을 1로 만든다.
# 원소의 위치를 찾아 res값을 변경

# import sys

# n = int(input())
# array = sys.stdin.readline().rstrip()
# array = array.split()
# m = int(input())
# target = sys.stdin.readline().rstrip()
# target = target.split()
# res = [0] * m

# intersect = set(map(int, set(array) & set(target)))
# for a in intersect:
#     i = target.index(a)
#     res[i] = 1
# for _ in res:
#     print(_, end=' ')

# => runtime error
    
# 방법 2.
# binary search 

# import sys

# def binary_search(array, target, start, end):
#     while (start <= end):
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return 1
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1            
#     return 0

# n = int(input())
# array = sys.stdin.readline().rstrip()
# array = list(map(int, array.split()))
# array.sort()
# m = int(input())
# target = sys.stdin.readline().rstrip()
# target = list(map(int, target.split()))
# res = []

# for t in target:
#     res.append(binary_search(array, t, 0, n-1))

# for _ in res:
#     print(_, end=' ')

# 정답 but 오래 걸림 -> dict() 사용하자


# 백준 - Silver - 1260
# 그래프를 DFS, BFS 탐색 결과 출력

# from collections import deque

# def dfs(v):
#     dfs_been[v] = 1
#     print(v, end=' ')
#     for next in graph[v]:
#         # 하나씩 조회
#         if dfs_been[next] == 0:
#             dfs(next)
#         else:
#             continue

# def bfs(v):
#     bfs_been[v] = 1
#     queue = deque()
#     queue.append(v)
#     while queue:
#         now = queue.popleft()
#         print(now, end=' ')
#         for next in graph[now]:
#             if bfs_been[next] == 0:
#                 bfs_been[next] = 1
#                 queue.append(next)
#             else:
#                 continue
            

# n, m, v = map(int, input().split()) # v는 시작점
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(n + 1):
#     graph[i].sort()

# dfs_been = [0] * (n+1)
# bfs_been = [0] * (n+1)

# dfs(v)
# print()
# bfs(v)


# 백준 - Silver - 2606
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 웜 바이러스에 걸리는 컴퓨터 수 출력 - 연결 확인

# from collections import deque

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# been = [0] * (n + 1)
# queue = deque()
# queue.append(1)
# been[1] = 1
# cnt = 0
# while queue:
#     now = queue.popleft()
#     for next in graph[now]:
#         if been[next] == 0:
#             been[next] = 1
#             queue.append(next)
#             cnt += 1
#         else:
#             continue
# print(cnt)

# 백준 - Silver - 2667

# 1은 집이 있는 곳, 0은 집이 없는 곳
# 연결된 집의 모임: 단지, 단지에 번호 붙이기
# 단지수 , 각 단지에 속하는 집의 수 '오름차순' 출력


# 재귀로 반복하면 당연히 '깊이' 우선으로 들어감
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False
#     if graph[x][y] == 1:
#         # print(x, y, graph[x][y])
#         graph[x][y] = 0
#         xy.append((x, y))
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# n = int(input())
# graph = [list(map(int, input())) for _ in range(n)]
# num = 0 # 단지의 개수
# res = []
# for i in range(n):
#     for j in range(n):
#         xy = []
#         if dfs(i, j):
#             res.append(len(xy))
#             num += 1
# res.sort()
# print(num)
# for x in res:
#     print(x)


# 백준 - Silver - 1012
# 1이 모여있는 개수 구하기 - Recursion Error: stack으로 구현해보자
import sys
sys.stdin.readline

def dfs(i, j):
    if i <= -1 or i >= m or j <= -1 or j >= n:
        return False
    if ground[i][j] == 1:
        ground[i][j] = 0
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        return True
    return False

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