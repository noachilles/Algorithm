from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    # 간선(a -> b)을 입력받음
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        a = q.popleft()
        result.append(a)
        for b in graph[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                q.append(b)

    for i in result:
        print(i, end =' ')
        
topology_sort()