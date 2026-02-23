from collections import deque
F, S, G, U, D = map(int, input().split())

visited = [0] * (F+1)

def bfs():
    global F, S, G, U, D
    q = deque()
    q.append((S, 0))
    while q:
        x, cnt = q.popleft()
        if x == G: # 도착하면 return
            return cnt
        for next in (x + U, x - D):
            if 0 < next <= F and visited[next] == 0:
                q.append((next, cnt+1))
                visited[next] = 1
    return -1

res = bfs()
if res >= 0:
    print(res)
else:
    print("use the stairs")