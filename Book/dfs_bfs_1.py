# 이코테 실전문제 5-1

# 입력
# (얼음 틀의 세로 길이 N, 가로 길이 M)
# (얼음 틀 형태 - 0: 얼음 / 1: 칸막이)
# 출력
# 한 번에 만들 수 있는 아이스크림 개수  

# 인접해있는 걸 찾으면 되니까 bfs로 생각해야 할 것 같음  

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 0인 경우에만 방문하도록
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)