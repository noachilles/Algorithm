import copy
N = int(input())
board = []
res = -1e9
for i in range(N):
    data = list(map(int, input().split()))
    board.append(data)
for i in range(1, N): # 각 행에 대해
    for j in range(i + 1): # 1행이 1개 값을 가지므로
        if 0 < j < i:
            board[i][j] = max(board[i-1][j-1], board[i-1][j]) + board[i][j]
        elif j == 0:
            board[i][j] = board[i-1][j] + board[i][j]
        else:
            board[i][j] = board[i-1][j-1] + board[i][j]
for i in range(N):
    if res < board[-1][i]:
        res = board[-1][i]
print(res)