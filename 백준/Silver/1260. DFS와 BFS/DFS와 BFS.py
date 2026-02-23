from collections import deque

def dfs(v):
    dfs_been[v] = 1
    print(v, end=' ')
    for next in graph[v]:
        # 하나씩 조회
        if dfs_been[next] == 0:
            dfs(next)
        else:
            continue

def bfs(v):
    bfs_been[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for next in graph[now]:
            if bfs_been[next] == 0:
                bfs_been[next] = 1
                queue.append(next)
            else:
                continue
            

n, m, v = map(int, input().split()) # v는 시작점
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

dfs_been = [0] * (n+1)
bfs_been = [0] * (n+1)

dfs(v)
print()
bfs(v)