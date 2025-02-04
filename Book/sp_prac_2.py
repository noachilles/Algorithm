# 설명
# X -> Y로 가려면 X와 Y간 양방향 통로가 있어야 한다
# N의 값이 매우 커질 수 있으므로 플로이드 사용 불가
# C -> 통로 거쳐 -> 최대한 많이 퍼져나갈 것 -> C에서 메세지를 받는 도시의 개수와 모두 메세지를 받는 데까지 걸리는 시간

# 입력
# 도시 개수 N, 통로 개수 M, 메세지 보내는 도시 C
# m줄동안 통로에 대한 정보 X, Y, Z 즉 X -> Y:Z

# 출력
# C에서 메세지 받는 도시 개수 , 걸리는 시간 공백 구분해 출력

# 일단 dijkstra 
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
distance = [INF] * (n + 1)


def dijkstra(start):
    city = maxTime = 0
    q = [] # q는 (거리, 노드)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 방문한 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 인접한 값 방문하고 q를 갱신
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for i in range(1, n + 1):
        if distance[i] != INF:
            city += 1
            if maxTime < distance[i]:
                maxTime = distance[i]
    return (city, maxTime)
    
           
# 기본 dijkstra 구현했음
# 기존 거리 출력이 아니라, 도시 개수와 총 소요 시간을 출력해야 한다.

city, maxTime = dijkstra(c)
print(city - 1, maxTime, end=" ")