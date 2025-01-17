# boj 1260
# TIL DFSnBFS_1.md 참고

# input
# (number of Node N, number of Edge M, start Node V)
# (node pair connected by edge)
# output
# result of DFS
# result or BFS

from collections import deque

# DFS
def dfs(graph, s, been):
    been[s] = 1
    print(s, end=' ')
    for nn in graph[s]:
        if been[nn] == 0:
            dfs(graph, nn, been)
        else:
            continue  
    
# BFS
def bfs(graph, s, been, queue):
    queue.append(s)
    been[s] = 1
    while queue:
        ns = queue.popleft()
        print(ns, end=' ')
        for nn in graph[ns]:
            if been[nn] == 0:
                queue.append(nn)
                been[nn] = 1
            else:
                continue
    
    
if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    for i in range(n+1):
        graph[i] = list(set(graph[i]))
        graph[i].sort()
    dfs_been = [0 for _ in range(n+1)]
    bfs_been = [0 for _ in range(n+1)]
    queue = deque()
    dfs(graph, v, dfs_been)
    print("")
    bfs(graph, v, bfs_been, queue)
    