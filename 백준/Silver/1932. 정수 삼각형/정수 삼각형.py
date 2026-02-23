n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
new = [[0] * n for _ in range(n)]
new[0][0] = grid[0][0]

def dp():
    for i in range(n-1):
        for j in range(i+1):
            new[i+1][j] = max(new[i+1][j], new[i][j] + grid[i+1][j])
            new[i+1][j+1] = max(new[i+1][j+1], new[i][j] + grid[i+1][j+1])

dp()
print(max(new[-1]))