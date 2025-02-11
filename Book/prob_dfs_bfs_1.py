# 설명
# 1번 ~ N번까지 도시와 M개 단방향 도로
# 모든 도로의 거리는 1
# X로 출발해 도달할 수 있는 도시 중 최단 거리 정확히 K인 모든 도시들의 번호를 출력하는 프로그램

# 입력
# 도시 개수 N, 도로 개수 M, 거리 정보 K, 출발 도시 번호 X
# M개 줄~ 자연수 A B (A->B)

# 출력
# 최단 거리가 K인 모든 도시 번호를 한 줄에 하나씩 오름차순 출력
# 존재하지 않으면 -1 출력
# 인접 리스트로 풀어야함(메모리 문제)

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
been = [-1] * (n+1)
been[x] = 0
q = deque()
q.append(x)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 단방향 경로
    
def bfs():    
    while q:
        now = q.popleft()
        for b in graph[now]:
            if been[b] < 0: # 방문 기록이 없다면
                been[b] = been[now] + 1
                q.append(b)
            else:
                continue
    
bfs()

for i in range(1, n+1):
    if been[i] == k:
        print(i)
        
if k not in been:
    print(-1)