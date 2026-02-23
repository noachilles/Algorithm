import copy
import sys
sys.setrecursionlimit(10**9)
def dfs(x, y, k):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if temp[x][y] > k:
        temp[x][y] = 0  # 0으로 바꿔줘야 한다  
        dfs(x+1, y, k)
        dfs(x-1, y, k)
        dfs(x, y+1, k)
        dfs(x, y-1, k)
        return True
    temp[x][y] = 0
    return False

n = int(input())
graph = []
res = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    
for t in range(100):
    temp = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, t):
                cnt += 1
    if res < cnt:
        res = cnt
    if cnt == 0:
        break
print(res)
