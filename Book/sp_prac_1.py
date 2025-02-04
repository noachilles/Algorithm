# 설명
# start: 1번
# 1번 ~ k번 + k번 ~ x번 : 따로 나눠서 생각하자 

# 입력
# 회사 개수 N, 경로 개수 M
# 연결된 두 회사 번호가 공백으로 구분됨 (나머지는 INF)
# X, K

# 출력
# A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력
# 만약 X번 회사에 도달할 수 없다면 -1을 출력

# 교재에서는 플루이드로 풀이함 - 구현이 간단하고, N의 범위가 100이하로 매우 한정적이기 때문 - 다른 파일에서 구현해보자

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())
    
# end까지만 수행할 수 있는 방법을... 찾아야 함
def dijkstra(start, end):
    # 일단 시작점에 대한 거리를 0으로 넣어야 함
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # q가 비어있지 않은 동안에 
    while q:
        dist, now = heapq.heappop(q)
        # now 노드를 방문한 적이 있다면:
        if distance[now] < dist:
            continue
        # graph와 q는 서로 index가 reverse
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]
    
to_k = dijkstra(1, k)
to_x = dijkstra(k, x)

if to_k == INF or to_x == INF:
    print(-1)
else:
    print(to_k + to_x)
