# BOJ - Silver - 1003
# 시간제한 0.25
# Bottom Up으로 풀이하자
# import sys
# input = sys.stdin.readline

# t = int(input())
# while t:
#     res = []
#     n = int(input())
#     res.append((1, 0))
#     res.append((0, 1))
#     if n < 2:
#         print(res[n][0], res[n][1])
#         t -= 1
#         continue
#     for i in range(2, n+1):
#         num_0 = res[i-1][0] + res[i-2][0]
#         num_1 = res[i-1][1] + res[i-2][1]
#         res.append((num_0, num_1))
#     print(res[n][0], res[n][1])
#     t -= 1

# BOJ - Silver - 9655
# n = int(input())
# if n % 2 == 0:
#     print('CY')
# else:
#     print('SK')

# BOJ - Silver - 1932
# import copy
# N = int(input())
# board = []
# res = -1e9
# for i in range(N):
#     data = list(map(int, input().split()))
#     board.append(data)
# for i in range(1, N): # 각 행에 대해
#     for j in range(i + 1): # 1행이 1개 값을 가지므로
#         if 0 < j < i:
#             board[i][j] = max(board[i-1][j-1], board[i-1][j]) + board[i][j]
#         elif j == 0:
#             board[i][j] = board[i-1][j] + board[i][j]
#         else:
#             board[i][j] = board[i-1][j-1] + board[i][j]
# for i in range(N):
#     if res < board[-1][i]:
#         res = board[-1][i]
# print(res)

# BOJ - Silver - 11726
# n = int(input())
# d = [0] * (n+1)

# d[1] = 1
# d[2] = 2

# def f():
#     for i in range(3, n+1):
#         if d[i] > 0: 
#             return d[i]
#         else:
#             d[i] = (d[i-1] + d[i-2])
        
# f()
# print(d[n])