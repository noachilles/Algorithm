from collections import deque
n, k = map(int, input().split())
MAX = 100001
d = [0] * MAX


def bfs():
    q = deque()
    q.append((n, 0))
    while q:
        x, count = q.popleft()
        # d[x] = count
        if x == k:
            return count
        for next in (x-1, x+1, x*2):
            if 0 <= next < MAX and d[next] == 0:
                q.append((next, count+1))
                d[next] = 1
            

print(bfs())