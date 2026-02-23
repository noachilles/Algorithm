from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

been = [0] * (n + 1)
queue = deque()
queue.append(1)
been[1] = 1
cnt = 0
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if been[next] == 0:
            been[next] = 1
            queue.append(next)
            cnt += 1
        else:
            continue
print(cnt)