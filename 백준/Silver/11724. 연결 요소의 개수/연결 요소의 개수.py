import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
been = [0] * (n + 1)

def dfs(v):
    been[v] = 1
    stack = [v]
    while stack:
        now = stack.pop()
        for next in graph[now]:
            if been[next] == 0:
                been[next] = 1
                stack.append(next)
    return 

res = 0
for i in range(1, n+1):
    if been[i] == 0:
        dfs(i)
        res += 1
print(res)