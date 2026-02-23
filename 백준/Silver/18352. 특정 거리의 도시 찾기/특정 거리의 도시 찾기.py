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