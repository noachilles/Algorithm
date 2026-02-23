import sys
sys.setrecursionlimit(10**9) # 재귀 최대 깊이 변경
input = sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    temp = list(map(int, input().rstrip().split()))
    for i in range(1, len(temp) - 1, 2):
        graph[temp[0]].append((temp[i], temp[i+1]))

maxdist = 0
maxnode = 0

def dfs(visited, start, dist):
    if visited[start]:
        return
    global maxdist # 할당 때문에 unboundlocalerror 발생
    global maxnode
    if maxdist < dist:
        maxdist = dist
        maxnode = start
    visited[start] = True
    for next, cost in graph[start]:
        dfs(visited, next, dist+cost)

visited = [False] * (v+1)        
dfs(visited, 1, 0)
visited = [False] * (v+1)
dfs(visited, maxnode, 0)
print(maxdist)