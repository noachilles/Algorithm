# 이코테 실전문제 5-1

# 입력
# (얼음 틀의 세로 길이 N, 가로 길이 M)
# (얼음 틀 형태 - 0: 얼음 / 1: 칸막이)
# 출력
# 한 번에 만들 수 있는 아이스크림 개수  

# 인접해있는 걸 찾으면 되니까 bfs로 생각해야 할 것 같음  
# 하지만 실젤는 DFS로 해결함

n, m = map(int, input().split())
# 그래프 형태로 모델링
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    # 노드가 이미 방문처리 되어있으면 False를 return
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print(result)