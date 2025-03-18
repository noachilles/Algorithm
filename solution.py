# BOJ - Silver - 1427

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
    
# BOJ - Bronze - 2798

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

# BOJ - Silver - 11650

# n = int(input())
# array = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     array.append((x, y))

# array = sorted(array, key=lambda x : (x[0], x[1]))
# for t in array:
#     print(t[0], t[1], end="\n")

# BOJ - Silver - 11651

# n = int(input())
# array = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     array.append((x, y))

# array = sorted(array, key=lambda x : (x[1], x[0]))
# for t in array:
#     print(t[0], t[1], end="\n")

# BOJ - Silver - 10814

# n = int(input())
# d = dict()
# for i in range(n):
#     age, name = map(str, input().split())
#     d[i] = (age, name)
    
# d = sorted(d.items(), key=lambda x: (x[1][0], x[0]))
# for v in d:
#     print(v[1][0], v[1][1], end='\n')

# BOJ - Silver - 10815

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


# BOJ - Silver - 1260
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


# BOJ - Silver - 2606
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

# BOJ - Silver - 2667

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


# BOJ - Silver - 1012
# 1이 모여있는 개수 구하기 - Recursion Error: stack으로 구현해보자

# def dfs(i, j):
#     if i <= -1 or i >= m or j <= -1 or j >= n:
#         return False
#     if ground[i][j] == 1:
#         ground[i][j] = 0
#         dfs(i-1, j)
#         dfs(i, j-1)
#         dfs(i+1, j)
#         dfs(i, j+1)
#         return True
#     return False

# import sys
# sys.stdin.readline

# def dfs(i, j):
#     stack = []
#     chk = False
#     stack.append((i, j))
#     while stack:
#         x, y = stack.pop()
#         if ground[x][y] == 1:
#             chk = True
#             for d in range(4):
#                 if x+dx[d] <= -1 or x+dx[d] >= m or y+dy[d] <= -1 or y+dy[d] >= n:
#                     continue
#                 else:
#                     if ground[x+dx[d]][y+dy[d]] == 1:
#                         stack.append((x+dx[d], y+dy[d]))
#                 ground[x][y] = 0
#     return chk

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# t = int(input())
# while t > 0:
#     m, n, k = map(int, input().split())
#     ground = [[0] * n for _ in range(m)]
#     for _ in range(k):
#         x, y = map(int, input().split())
#         ground[x][y] = 1
#     cnt = 0
#     for i in range(m):
#         for j in range(n):
#             if dfs(i, j):
#                 cnt += 1
#     print(cnt)
#     t -= 1


# BOJ - Silver - 11724

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# been = [0] * (n + 1)

# def dfs(v):
#     been[v] = 1
#     stack = [v]
#     while stack:
#         now = stack.pop()
#         for next in graph[now]:
#             if been[next] == 0:
#                 been[next] = 1
#                 stack.append(next)
#     return 

# res = 0
# for i in range(1, n+1):
#     if been[i] == 0:
#         dfs(i)
#         res += 1
# print(res)


# BOJ - Gold - 10026 (미결)
# import sys
# sys.stdin.readline

# n = int(input())
# picture = []
# for _ in range(n):
#     picture.append(list(input().rstrip()))
    
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# # 서로 다른 구역을 찾는 문제: 얼음 만들기와 같다 - dfs
# # 하지만 0, 1로 이루어져 있지 않고 0, 1 값으로 변경할 수 없음
# # 그리고 이전 것과 같은지 다른지가 중요한 요소일 것 같다
# def dfs(i, j):
#     stack = []
#     stack.append((i, j))
#     chk = False
#     while stack:
#         x, y = stack.pop()
#         now = picture[x][y]
#         for d in range(4):
#             if x + dx[d] <= -1 or x + dx[d] >= n or y + dy[d] <= -1 or y + dy[d] >= n:
#                 continue
#             elif picture[x+dx[d]][y+dy[d]] == 0:
#                 continue
#             else:
#                 if picture[x+dx[d]][y+dy[d]] == now:
#                     chk = True
#                     stack.append((x+dx[d], y+dy[d]))
#             picture[x][y] = 0
#     return chk

# def dfs2(i, j):
#     stack = []
#     stack.append((i, j))
#     chk = False
#     while stack:
#         x, y = stack.pop()
#         if picture[x][y] == 'G':
#             picture[x][y] = 'R'
#         now = picture[x][y]
#         for d in range(4):
#             if x + dx[d] <= -1 or x + dx[d] >= n or y + dy[d] <= -1 or y + dy[d] >= n:
#                 continue
#             elif picture[x+dx[d]][y+dy[d]] == 0:
#                 continue
#             else:
#                 if picture[x+dx[d]][y+dy[d]] == now:
#                     chk = True
#                     stack.append((x+dx[d], y+dy[d]))
#             picture[x][y] = 0
#     return chk
    

# res = 0
# for i in range(n):
#     for j in range(n):
#         if dfs2(i, j):
#             res += 1
# print(res)


# BOJ - Gold - 1167(미결 - 참고)

# 설명
# 트리의 지름: 임의의 두 점 사이 거리 중 가장 긴 것
# 입력
# 정점 개수 V, 간선 정보
# 다들 2~3시간 정도는 괜찮대. 좀 더 용기내서 해보자
# 자료구조는 이렇게 쓰는 거구나
# 임의의 정점 하나에서 가장 먼 정점을 구하고, 거기까지의 거리를 구한다
# import sys
# sys.setrecursionlimit(10**9) # 재귀 최대 깊이 변경
# input = sys.stdin.readline
# v = int(input())
# graph = [[] for _ in range(v+1)]
# for _ in range(v):
#     temp = list(map(int, input().rstrip().split()))
#     for i in range(1, len(temp) - 1, 2):
#         graph[temp[0]].append((temp[i], temp[i+1]))

# maxdist = 0
# maxnode = 0

# def dfs(visited, start, dist):
#     if visited[start]:
#         return
#     global maxdist # 할당 때문에 unboundlocalerror 발생
#     global maxnode
#     if maxdist < dist:
#         maxdist = dist
#         maxnode = start
#     visited[start] = True
#     for next, cost in graph[start]:
#         dfs(visited, next, dist+cost)

# visited = [False] * (v+1)        
# dfs(visited, 1, 0)
# visited = [False] * (v+1)
# dfs(visited, maxnode, 0)
# print(maxdist)


# BOJ - Silver - 2839
# 설명
# 최대한 적은 개수의 3kg or 5kg 봉지를 더해 nkg 만들기(봉지 개수)

# 단순히 5이상이면 안 됨 6의 경우를 생각하자 - 6, 9, 12 다 안 됨
# 5와 3의 배수의 경우엔, 5로 나누는 편이 나음
# 하지만 아래의 방법으론 원하는 값을 얻을 수 없음
# n < 3: No, n == 3: yes, n == 4: No, n == 5: Yes, n == 6: Yes, 6 < n < 9: No, n == 9: yes, n == 10: yes...
# 5의 배수가 될 때까지만! 3을 빼는 거야!

# n = int(input())
# cnt = 0
# while n % 5 != 0 and n > 0:
#     cnt += 1
#     n -= 3
            
# if n % 5 == 0 and n > 0:
#     cnt += n // 5
#     n %= 5
    
# if n == 0:
#     print(cnt)
# else:
#     print(-1)


# BOJ - Silver - 11399
# import sys
# input = sys.stdin.readline

# n = int(input())
# p_list = list(map(int, input().split()))
# p_list.sort()
# for i in range(n-1):
#     p_list[i+1] = p_list[i] + p_list[i+1]
# print(sum(p_list))


# BOJ - Gold - 9466 (미결)
# 설명
# 사이클 판단 - 사이클에 포함되지 못한 노드의 수 구하기

# 결국 사이클이란: 자기 자신으로 돌아오는 것
# 그래프 이론에서 우두머리를 정하고 그걸 비교해서 판단


# BOJ - Silver - 11725
# 설명
# 루트 없는 트리, 트리의 루트: 1일 때 각 노드의 부모 구하기

# import sys
# sys.setrecursionlimit(10**9) # 재귀 최대 깊이 변경
# input = sys.stdin.readline

# def dfs(start):
#     # 방문 처리
#     visited[start] = True
#     # 1개의 값을 가지고 있고 방문했다면
#     if len(graph[start]) == 1:
#         node = graph[start][0]
#         if visited[node] == True:
#             parent[start] = node
#             return
#         else:
#             dfs(node)
#     # graph[start] 내부 원소에 대해
#     for node in graph[start]:
#         # 방문한 적이 없다면
#         if visited[node] == False:
#             dfs(node)
#         # 1이라면 parent = 1
#         else:
#             parent[start] = node
        
            
# n = int(input())
# graph = [[] for _ in range(n+1)]
# parent = [0] * (n+1)
# visited = [False] * (n+1)
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# dfs(1)
# # print(graph)
# for i in range(2, n+1):
#     print(parent[i])


# 이코테 - PART2 - 정렬
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))

# array = sorted(array, reverse=True)
# for i in range(n):
#     print(array[i], end=' ')


# 이코테 - PART2 - 정렬
# n = int(input())
# array = []
# for _ in range(n):
#     name, score = map(str, input().split())
#     array.append((name, int(score)))

# array = sorted(array, key=lambda x: x[1])
# for i in array:
#     print(i[0], end=' ')


# 이코테 - PART2 - 정렬
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a = sorted(a)
# b = sorted(b, reverse = True)
# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
#     else:
#         break

# print(sum(a))


# 이코테 - PART2 - 순차탐색
# def sequential_search(n, target, array):
#     for i in range(n):
#         if target == array[i]:
#             return i + 1
# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]

# array = list(input().split())
# print(sequential_search(n, target, array))


# 이코테 - PART2 - 이진탐색
# 재귀로 구현
# def binary_search(start, n, target, array):
#     if start > n:
#         return -1
#     mid = (start + n) // 2
#     key = array[mid]
#     if target == key:
#         return mid
#     elif target < key:
#         return binary_search(start, mid-1, target, array)
#     else:
#         return binary_search(mid+1, n, target, array)

# n, target = map(int, input().split())
# array = list(map(int, input().split()))
# print(binary_search(0, n, target, array))


# 이코테 - PART2 - 이진탐색
# 반복문으로 구현
# def binary_search(start, end, target, array):
#     while start < end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return (mid + 1)
#         elif target < array[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1

# n, target = map(int, input().split())
# array = list(map(int, input().split()))
# print(binary_search(0, n, target, array))


# 이코테 - PART2 - 이진탐색
# import time
# import sys
# input = sys.stdin.readline
# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return (i + 1)
#     return -1

# def binary_search(start, end, target, array):
#     while(start <= end):
#         mid = (start + end) // 2
#         if target == array[mid]:
#             return (mid + 1)
#         elif target < array[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1

# n = int(input())
# a = list(map(int, input().rstrip().split()))
# a = sorted(a)
# m = int(input())
# b = list(map(int, input().rstrip().split()))

# for item in b:
#     s_time = time.time_ns()
#     res1 = sequential_search(n, item, a)
#     e_time = time.time_ns()
#     time1 = e_time - s_time
#     s_time = time.time_ns()
#     res2 = binary_search(0, n, item, a)
#     e_time = time.time_ns()
#     time2 = e_time - s_time

#     print(f'sequential search(time, result): {time1}, {res1}\nbinary search(time, result): {time2}, {res2}')
#     print('-----')

# for item in b:
#     res = binary_search(0, n, item, a)
#     if res > 0:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 계수정렬 풀이
# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# for i in input().split():
#     if array[int(i)] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


# 이코테 - PART2 - 이진 탐색
# 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 이는 높이 최댓값
# def binary_search(start, end, target, array):
#     while (start <= end):
#         res = 0
#         mid = (start + end) // 2 
#         for item in array:
#             if item > mid:
#                 res += (item - mid)
#         if target == res: # 딱 res 라면
#             return mid
#         elif target < res: # m < 떡 길이
#             start = mid + 1
#         else: # m > 떡 길이
#             end = mid - 1 
#     return mid


# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# array.sort()
# print(binary_search(0, array[-1], m, array))


# 이코테 - PART2 - DP
# 피보나치 함수(재귀적)
# d = [0] * 100 # 연산한 값의 결과를 저장

# def fibo(x):
#     if x == 1 or x == 2: # 종료 조건, 1이나 2일 때 1을 반환
#         return 1 
#     # 이미 계산한 적 있는 문제라면 -> 그대로 반환
#     if d[x] > 0:
#         return d[x]
#     else:
#         d[x] = fibo(x-1) + fibo(x-2)
#         return d[x]

# print(fibo(6))

# 피보나치 함수(반복문)
# d = [0] * 100

# def fibo(x):
#     d[1] = 1
#     d[2] = 1
#     for i in range(3, x+1):
#         d[i] = d[i-1] + d[i-2]
#     return d[x]

# print(fibo(6))


# 이코테 - PART2 - DP
# x = int(input())
# d = [30001] * (x+1)
# d[x] = 0
# while x > 1:
#     if x % 5 == 0:
#         d[x // 5] = min(d[x] + 1, d[x // 5])
#     elif x % 3 == 0:
#         d[x // 3] = min(d[x] + 1, d[x // 3])
#     elif x % 2 == 0:
#         d[x // 2] = min(d[x] + 1, d[x // 2])
#     d[x - 1] = min(d[x] + 1, d[x - 1])
#     x -= 1
# print(d[1])


# 이코테 - PART2 - DP
# n = int(input())
# array = list(map(int, input().split()))
# d = [0] * n
# d[0] = array[0]
# d[1] = max(array[1], array[0])
# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2] + array[i])
# print(d[n-1])


# 이코테 - PART2 - DP
# n = int(input())

# d = [0] * (n+1)
# d[1] = 1
# d[2] = 3
# for i in range(3, n+1):
#     d[i] = (d[i-1] + d[i-2] * 2) % 796796
    
# print(d[n])


# 이코테 - PART2 - DP
# n종류 화폐 개수 최소한으로 m원 만들기
# n, m = map(int, input().split())
# d = [10001] * (m + 1)
# array = []

# for i in range(n):
#     k = int(input())
#     array.append(k)

# # 범위 밖을 벗어나지 않도록 하기 위해 0을 초기화
# d[0] = 0
    
# for k in array:
#     for i in range(k, m+1):
#         if d[i-k] != 10001:
#             d[i] = min(d[i], d[i-k] + 1)
        
# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])


# BOJ - Silver - 1920
# 정수 범위가 -2^31 ~ 2^31로 매우 크다
# 따라서, 계수정렬로 풀 수 없다

# import sys
# input = sys.stdin.readline

# def binary_search(start, end, target, array):
#     while(start <= end):
#         mid = (start + end) // 2
#         if target == array[mid]:
#             return mid
#         elif target < array[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1

# n = int(input())
# a = list(map(int, input().rstrip().split()))
# m = int(input())
# b = list(map(int, input().rstrip().split()))

# a.sort()

# for target in b:
#     res = binary_search(0, n-1, target, a)
#     if res == -1:
#         print(0)
#     else:
#         print(1)


# BOJ - Silver - 10814
# 나이와 이름이 가입한 순서대로
# 나이 오름차순, 나이 같으면 먼저 가입한 사람이 앞에

# n = int(input())
# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((int(input_data[0]), input_data[1], i))

# array.sort(key=lambda member: (member[0], member[2]))
# for member in array:
#     print(member[0], member[1])


# BOJ - Silver - 10816
# b에 적힌 숫자 카드의 개수 구하기
# 값이 크기 때문에 사용할 수 없는 것: 계수 정렬
# -> 이진 탐색을 사용해야 할 것 같은데, 어떻게 하면 좋을까
# 일단 결과가 담길 list를 전부 0으로 초기화
# set에 값을 담아서 있는지 여부를 확인하고, 없는 값들은 찾지 않고 있는 값들만 계산하면 안 되나..
# import sys
# input = sys.stdin.readline

# def binary_search(start, end, target, array):
#     while(start <= end):
#         mid = (start + end) // 2
#         if target == array[mid][0]:
#             return array[mid][1]
#         elif target < array[mid][0]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 0

# n = int(input())
# a = list(map(int, input().rstrip().split()))
# m = int(input())
# b = list(map(int, input().rstrip().split()))

# a.sort()
# s = set(a)
# res = [0] * m # 결과

# array = []
# cnt = 1
# for i in range(0, n-1): # O(N)
#     if a[i] != a[i+1]: # 다음 값과 다르다면
#         k = a[i]
#         array.append((a[i], cnt))
#         cnt = 1
#     else: # 다음 값과 같다면
#         cnt += 1
# array.append((a[-1], cnt))

# for i in range(m):
#     res[i] = binary_search(0, len(array) - 1, b[i], array)

# for item in res:
#     print(item, end=' ')
    
# 코드 분석
# import sys
# from collections import Counter
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().rstrip().split()))
# m = int(input())
# b = list(map(int, input().rstrip().split()))

# cnt_dict = Counter(a)
# for target in b:
#     print(cnt_dict[target], end=' ')


# BOJ - Silver - 1463
# 시간제한 0.15초
# x가 3으로 나누어 떨어지면 3으로 나눔
# 2로 나누어 떨어지면 2로 나눔
# 1을 뺀다
# n = int(input())
# d = [10**6] * (n+1)
# d[0] = 0
# d[1] = 0
# for x in range(2, n+1):
#     if x % 6 == 0:
#         d[x] = min(d[x//3] + 1, d[x//2] + 1)
#     elif x % 3 == 0:
#         d[x] = min(d[x//3] + 1, d[x-1] + 1)
#     elif x % 2 == 0:
#         d[x] = min(d[x//2] + 1, d[x-1] + 1)
#     else:
#         d[x] = d[x-1] + 1
# print(d[n])


# BOJ - Silver - 9095
# d = {1:1, 2:2, 3:4}
# def f(x):
#     if x in d:
#         return d[x]
#     else:
#         d[x] = f(x-1) + f(x-2) + f(x-3)
#     return d[x]

# if __name__ == "__main__":
#     t = int(input())
#     while t:
#         n = int(input())
#         print(f(n))
#         t -= 1


# BOJ - Silver - 2941
# import sys
# input = sys.stdin.readline

# s = input().rstrip()

# def chk(s): # dz, z 제외 크로아티아 알파벳 찾고 개수 세기
#     cnt = 0
#     for i in range(len(s)-1):
#         if s[i:i+2] == None:
#             break
#         elif s[i:i+2] in d:
#             cnt += 1
#             visited.append(i)
#             visited.append(i+1)
#     return cnt

# def chk_dz(s): # dz 찾고 개수 세기
#     cnt = 0
#     for i in range(len(s)-2):
#         if s[i:i+3] == None:
#             break
#         elif s[i:i+3] == 'dz=':
#             cnt += 1
#             visited.append(i)
#             visited.append(i+1)
#             visited.append(i+2)
#     return cnt

# def chk_z(s): 
#     cnt = 0
#     for i in range(len(s)-1):
#         temp = set(visited)
#         if i not in temp:
#             if s[i:i+2] == None:
#                 break
#             elif s[i:i+2] == 'z=':
#                 visited.append(i)
#                 visited.append(i+1)
#                 cnt += 1
#     return cnt

# def chk_else(s):
#     cnt = 0
#     for i in range(len(s)):
#         if not i in visited:
#             cnt += 1
#     return cnt

# if __name__ == '__main__':
#     cnt = 0
#     d = {'c=':0, 'c-':0, 'd-':0, 'lj':0, 'nj': 0, 's=':0}
#     visited = []
#     cnt += chk(s)
#     cnt += chk_dz(s)
#     cnt += chk_z(s)
#     visited = set(visited)
#     cnt += chk_else(s)    
#     print(cnt)
    
    
# BOJ - Silver - 4673
# def d(n):
#     if n > 9999:
#         l = 5
#     elif n > 999:
#         l = 4
#     elif n > 99:
#         l = 3
#     elif n > 9:
#         l = 2
#     else:
#         l = 1
#     res = n
#     while l > 0:
#         k = (10 ** (l-1))
#         res += (n // k)
#         n %= k
#         # print(l, res)
#         l -= 1
#     return res

# ref = dict()
# for x in range(1, 10001):
#     if d(x) < 10001:
#         ref[d(x)] = 0
# for x in range(1, 10001):
#     if not x in ref:
#         print(x)


# 이코테 - PART2 - 최단 경로
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# # 노드 개수, 간선 개수 입력 받기
# n, m = map(int, input().split())
# start = int(input())
# # 각 노드에 연결된 노드에 대한 정보 담는 리스트
# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# # 모든 간선 정보를 입력 받기 - 연결된 노드와 거리
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
# def get_nearest_node():
#     min_value = INF
#     index = 0 # 가장 최단 거리가 짧은 노드
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     # 시작 노드에 대해 초기화
#     distance[start] = 0
#     visited[start] = True
#     # 시작 노드와 연결된 노드 j에 대해
#     for j in graph[start]:
#         # 거리를 갱신
#         distance[j[0]] = j[1]
#     # 시작 노드 제외한 전체 n-1 노드에 대해 반복
#     for i in range(n-1):
#         now = get_nearest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노드를 거쳐서 가는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# dijkstra(start)
# for i in range(1, n+1):
#     print(distance[i])

# 개선된 다익스트라
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)
# visited = [False] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def dijkstra(start):
#     q = []
#     # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입 
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q: # 큐가 비어있지 않다면
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적이 있으면 무시
#         if visited[now] == True:
#             continue
#         # 현재 노드와 연결된 다른 인접 노드 확인
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
        
# dijkstra(start)
# for i in range(n+1):
#     print(distance[i])

# # 플로이드 워셜
# n = int(input())
# INF = int(1e9)
# graph = [[INF] * (n+1) for _ in range(n+1)]
# # 자신까지의 거리는 0으로 초기화
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0

# m = int(input())
# # 거리 정보
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# for k in range(n+1):
#     for a in range(n+1):
#         for b in range(n+1):
#             if k == a or k == b or a == b: # 이건 생략 가능
#                 continue
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print('INF', end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()

# 이코테 - PART2 - 최단경로
# 1애서 출발, K를 거쳐 X로 가는 최단 경로
# 플로이드워셜은 O(N^3)인데 N이 최대 100이므로 100^3 = 1,000,000이라 O
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# x, k = map(int, input().split())

# for c in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
            
# res = graph[1][k] + graph[k][x]
# if res >= INF:
#     print(-1)
# else:
#     print(res)

# 이코테 - PART2 - 최단경로
# 범위가 커서 플로이드 워셜 쓸 수 X
# 도시에서 일방적으로 연결되어 있는 도시 총 몇 개?
# 그것들 중 가장 긴 시간이 걸리는 것 -> 다익스트라로 구하기
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)
# n, m, c = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)
# visited = [False] * (n+1)
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z)) # 도시, 거리
    
# q = []
# def dijkstra(start):
#     heapq.heappush(q, (0, start))
#     visited[start] = True
#     distance[start] = 0
#     cnt = 0
#     t = 0
#     while q: # q에 값이 있을 동안
#         dist, now = heapq.heappop(q)
#         for i in graph[now]: # 연결된 다른 (도시, 거리)들에 대해
#             # 기존보다 거리가 더 짧으면 갱신
#             if visited[i[0]] == True:
#                 continue
#             cost = dist + i[1]
#             if cost < distance[i[0]]: # 도시
#                 distance[i[0]] = cost
#                 if t < cost:
#                     t = cost
#                 cnt += 1
#             heapq.heappush(q, (i[1], i[0]))
#     return cnt, t

# cnt, t = dijkstra(c)
# print(cnt, t, end=' ')

# 이코테 - PART2 - 그래프 이론
# import sys
# input = sys.stdin.readline

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int, input().split())
# parent = [0] * (v + 1)

# for i in range(1, v+1):
#     parent[i] = i

# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
    
# print('각 원소가 속한 집합: ', end=' ')
# for i in range(1, v+1):
#     print(find_parent(parent, i), end=' ')

# print()

# print('부모 테이블: ', end=' ')
# for i in range(1, v+1):
#     print(parent[i], end=' ')

# # 최소 신장 트리 - 크루스칼
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int, input().split())
# edges = []
# parent = [0] * (v+1)
# res = 0

# for i in range(1, v+1):
#     parent[i] = i

# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
    
# edges.sort()

# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         res += cost
# print(res)

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
# arr1 = [[[-1, -1, 0, 0, 0],
#        [-1, -1, 0, 1, 1],
#        [0, 0, 0, 1, 1]]]

# arr2 = [[[0, -1, 0, 0, 0],
#        [-1, -1, 0, 1, 1],
#        [0, 0, 0, 1, 1]]]

# arr3 = [[[-1, -1, 1, 1, 1],
#        [-1, -1, 1, 1, 1],
#        [1, 1, 1, 1, 1]]]

# from collections import deque

# dx = [0, 0, 0, 0, 1, -1]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [1, -1, 0, 0, 0, 0]


# # 덜익은 토마토 개수 세기
# def cnt_except_green(grid):
#     global m, n, h
#     cnt = 0
#     for z in range(h):
#         for y in range(n):
#             for x in range(m):
#                 if grid[z][y][x] == 1 or grid[z][y][x] == -1:
#                     cnt += 1
#     return cnt

# # bfs
# def bfs(grid, visited, start):
#     global m, n, h
#     t_green = 0
#     q = deque(start)
#     not_yet = []
#     while q:
#         cz, cy, cx = q.popleft()
#         visited[cz][cy][cx] = 1
#         for i in range(6):
#             nz = cz + dz[i]
#             ny = cy + dy[i]
#             nx = cx + dx[i]
            
#             if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
#                 if grid[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
#                     not_yet.append((nz, ny, nx))
#                     visited[nz][ny][nx] = 1
#     return not_yet


# if __name__ == "__main__":
#     m, n, h = map(int, input().split())
#     grid = [list(list(map(int, input().split())) for j in range(n)) for i in range(h)]
    
#     # 모두 익은 토마토면 0 출력
#     ngreen = cnt_except_green(grid)
#     if ngreen == m * n * h:
#         print(0)
#         exit()
    
#     visited = [[[0] * m for i in range(n)] for j in range(h)]

#     day = 0

#     start = []
    
#     for z in range(h):
#         for y in range(n):
#             for x in range(m):
#                 if grid[z][y][x] == 1 and not visited[z][y][x]:
#                     # 익는 토마토의 좌표가 반환된다
#                     start.append((z, y, x))
#     while True:
#         start = bfs(grid, visited, start)
#         # 더 이상 변화가 없으면 익지 않은 토마토 개수를 세면 된다   
#         if not start:
#             break
#         ngreen += len(start)
#         day += 1
#     if ngreen == m * n * h:
#         print(day)
#     else:
#         print(-1)

# BOJ - Silver - 1003
# 시간제한 0.25
# Bottom Up으로 풀이하자
# import sys
# input = sys.stdin.readline

# t = int(input())
# while t:
#     res = []
#     n = int(input())
#     res.append((1, 0))
#     res.append((0, 1))
#     if n < 2:
#         print(res[n][0], res[n][1])
#         t -= 1
#         continue
#     for i in range(2, n+1):
#         num_0 = res[i-1][0] + res[i-2][0]
#         num_1 = res[i-1][1] + res[i-2][1]
#         res.append((num_0, num_1))
#     print(res[n][0], res[n][1])
#     t -= 1

# BOJ - Silver - 9655
# n = int(input())
# if n % 2 == 0:
#     print('CY')
# else:
#     print('SK')

# BOJ - Silver - 1932
# import copy
# N = int(input())
# board = []
# res = -1e9
# for i in range(N):
#     data = list(map(int, input().split()))
#     board.append(data)
# for i in range(1, N): # 각 행에 대해
#     for j in range(i + 1): # 1행이 1개 값을 가지므로
#         if 0 < j < i:
#             board[i][j] = max(board[i-1][j-1], board[i-1][j]) + board[i][j]
#         elif j == 0:
#             board[i][j] = board[i-1][j] + board[i][j]
#         else:
#             board[i][j] = board[i-1][j-1] + board[i][j]
# for i in range(N):
#     if res < board[-1][i]:
#         res = board[-1][i]
# print(res)

# BOJ - Silver - 11726
# n = int(input())
# d = [0] * (n+1)

# d[1] = 1
# d[2] = 2

# def f():
#     for i in range(3, n+1):
#         if d[i] > 0: 
#             return d[i]
#         else:
#             d[i] = (d[i-1] + d[i-2])
        
# f()
# print(d[n])

# # 이코테 - PART2 - GRAPH
# def find_team(team, x):
#     if team[x] != x:
#         team[x] = find_team(team, team[x])
#     return team[x]

# def union_team(team, a, b):
#     a = find_team(team, a)
#     b = find_team(team, b)
#     if a < b:
#         team[b] = a
#     else:
#         team[a] = b

# def check_team(team, a, b):
#     a = find_team(team, a)
#     b = find_team(team, b)
#     if a == b:
#         print('YES')
#     else:
#         print('NO')

# n, m = map(int, input().split())
# cal = []
# team = [0] * (n+1)
# for i in range(n+1):
#     team[i] = i
# for _ in range(m):
#     c, a, b = map(int, input().split())
#     if c == 0:
#         union_team(team, a, b)
#     else:
#         check_team(team, a, b)

# 이코테 - PART2 - GRAPH
# def find_city(city, x):
#     if city[x] != x:
#         city[x] = find_city(city, city[x])
#     return city[x]

# def union_city(city, a, b):
#     a = find_city(city, a)
#     b = find_city(city, b)
#     if a < b:
#         city[b] = a
#     else:
#         city[a] = b

# n, m = map(int, input().split())
# edges = []
# city = [0] * (n+1)
# res = 0
# last = 0
# for i in range(n+1):
#     city[i] = i
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
# edges.sort()
# # 가장 큰 값을 제거해 두 마을을 끊음
# # 작은 것부터 선택해서 (크루스칼) 최소 신장 트리 만들기
# # 단 서로 다른 마을을 분리해야 하므로
# for edge in edges:
#     cost, a, b = edge
#     if find_city(city, a) != find_city(city, b):
#         union_city(city, a, b)
#         res += cost
#         last = cost
# res -= last
# print(res)

# 이코테 - PART2 - GRAPH
# import copy
# from collections import deque
# n = int(input())
# lecture = [[] for i in range(n+1)]
# q = []
# indegree = [0] * (n+1)
# time = [0] * (n+1)

# for i in range(1, n+1):
#     data = list(map(int, input().split()))
#     time[i] = data[0]
#     for x in data[1:-1]:
#         indegree[i] += 1
#         lecture[x].append(i)
    
# def topology_sort():
#     res = copy.deepcopy(time)
#     q = deque()
    
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             q.append(i)
    
#     while q:
#         now = q.popleft()
#         # now를 수강하면 수강할 수 있는 것들
#         for i in lecture[now]:
#             res[i] = max(res[i], res[now] + time[i])
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
    
#     for i in range(1, n+1):
#         print(res[i])

# topology_sort()

# BOJ - Silver - 10773
# a = []
# res = 0
# last = 0
# k = int(input())
# for _ in range(k):
#     n = int(input())
#     if n == 0:
#         res -= last
#         a.pop()
#         if a:
#             last = a[-1]
#         continue
#     a.append(n)
#     res += n
#     last = a[-1]
# print(res)

# BOJ - 14503
# 아마 그냥 Simulation

# arr1 = [[1, 1, 1, 1],
#         [1, 0, 0, 1],
#         [1, 1, 0, 1],
#         [1, 1, 1, 1]]

# arr2 = [[1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1],
#         [1, 0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 1, 1]]

# dlist = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향 북-동-남-서 0, 1, 2, 3

# def f(grid, r, c, d):
#     cnt = 0
#     while True:
#         # 현재 칸이 청소되지 않은 칸
#         if grid[r][c] == 0:
#             # 청소 후 개수 세기, 청소되면 -1로 변경
#             cnt += 1
#             grid[r][c] = -1
            
#         # 빈 칸 여부 판단
#         chk = False
#         for i in range(4):
#             dr, dc = r + dlist[i][0], c + dlist[i][1]
#             if grid[dr][dc] == 0:
#                 chk = True
                
#         # 주위에 빈 칸이 있다면
#         if chk == True:
#             # 반시계 90도 회전
#             if d != 0:
#                 d -= 1
#             else:
#                 d = 3
#             nr, nc = r + dlist[d][0], c + dlist[d][1]
#             if grid[nr][nc] == 0:
#                 r, c = nr, nc
#             continue
        
#         # 빈 칸이 없다면
#         if not chk:
#             # 방향 유지한 채 후진
#             nr, nc = r - dlist[d][0], c - dlist[d][1]
#             if grid[nr][nc] == 1:
#                 return cnt
#             else:
#                 r, c = nr, nc
#                 continue
    
# if __name__ == "__main__":
#     # r, c, d = 3, 2, 0
#     # grid = arr2
#     # print(f(grid, r, c, d))
#     N, M = map(int, input().split())
#     r, c, d = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     print(f(grid, r, c, d))

# BOJ - 14499
# 주사위 세로 가로, hor의 1을 바닥면으로 본다
# 또한 ver의 i=3 값이 결과이다.

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