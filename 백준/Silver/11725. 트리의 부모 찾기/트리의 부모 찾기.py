
import sys
sys.setrecursionlimit(10**9) # 재귀 최대 깊이 변경
input = sys.stdin.readline

def dfs(start):
    # 방문 처리
    visited[start] = True
    # 1개의 값을 가지고 있고 방문했다면
    if len(graph[start]) == 1:
        node = graph[start][0]
        if visited[node] == True:
            parent[start] = node
            return
        else:
            dfs(node)
    # graph[start] 내부 원소에 대해
    for node in graph[start]:
        # 방문한 적이 없다면
        if visited[node] == False:
            dfs(node)
        # 1이라면 parent = 1
        else:
            parent[start] = node
        
            
n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
# print(graph)
for i in range(2, n+1):
    print(parent[i])