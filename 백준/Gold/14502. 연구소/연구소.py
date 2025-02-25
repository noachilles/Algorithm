import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
temp = [[0] * m for _ in range(n)]
result = cnt = 0
v = []

for i in range(n):
    data = list(input().rstrip().split())
    for x in data:
        graph[i].append(int(x))
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
        elif graph[i][j] == 2:
            v.append((i, j))

# virus가 퍼진다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def virus(x, y, temp):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny, temp)
    return

def get_score(temp):
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def make_wall():
    global cnt
    global result
    cnt_temp = cnt - 3
    for i in range(0, n*m):
        for j in range(i+1, n*m):
            for k in range(j+1, n*m):
                x1 = i // m
                y1 = i % m
                
                x2 = j // m
                y2 = j % m
                
                x3 = k // m
                y3 = k % m
                
                if graph[x1][y1] == 0 and graph[x2][y2] == 0 and graph[x3][y3] == 0:
                    
                    temp = copy.deepcopy(graph)
                    temp[x1][y1] = 1
                    temp[x2][y2] = 1
                    temp[x3][y3] = 1
                    
                    for dot in v:
                        virus(dot[0], dot[1], temp)
                    result = max(result, get_score(temp))
    return result
                
print(make_wall())