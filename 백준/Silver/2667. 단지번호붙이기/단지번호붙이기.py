def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        # print(x, y, graph[x][y])
        graph[x][y] = 0
        xy.append((x, y))
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
num = 0 # 단지의 개수
res = []
for i in range(n):
    for j in range(n):
        xy = []
        if dfs(i, j):
            res.append(len(xy))
            num += 1
res.sort()
print(num)
for x in res:
    print(x)