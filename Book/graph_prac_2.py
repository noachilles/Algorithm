# 설명
# N개의 집, M개의 길 -> 길은 양방향
# 마을을 두 개로 분할 ~ 마을에는 집이 하나 이상 있어야 하고, 마을 내부 집들은 서로 연결되어야 함
# 분리된 두 마을 사이: 길이 필요하지 않음 -> 제거
# 두 마을 내부: 임의의 두 집 사이 경로가 항상 존재하게 하며 길 더 없앨 수 있음
# 유지비의 합을 최소로 하도록

# 입력
# N, M: 집의 개수, 길의 개수(각각 <=100,000, <=1,000,000)
# A, B, C 3개의 정수로 공백 구분, A번 집과 B번 집을 연결하는 유지비가 C

# 출력
# 유지비 합의 최솟값

# 서로 사이클이 발생하지 않도록(클루스칼 알고리즘 사용하며, 2개로 구분하는 게 어려움..)

import sys
input = sys.stdin.readline
# 일단 입력을 받아보자

def find_city(city, x):
    if city[x] != x:
        city[x] = find_city(city, city[x])
    return city[x]

def union_city(city, a, b):
    a = find_city(city, a)
    b = find_city(city, b)
    if a < b:
        city[b] = a
    else:
        city[a] = b

n, m = map(int, input().split())
edges = []
chosen = []
city = [0] * (n + 1)
result = 0
last = 0

for i in range(1, n + 1):
    city[i] = i
    
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_city(city, a) != find_city(city, b):
        union_city(city, a, b)
        result += cost
        last = cost
# 두 개의 마을로 구분
result -= last
print(result)