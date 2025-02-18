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