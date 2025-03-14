# BOJ - Silver - 10825
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = [[] for _ in range(n)]
# for i in range(n):
#     data = list(input().split())
#     array[i] = [data[0], int(data[1]), int(data[2]), int(data[3])]

# array.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))
# for i in range(n):
#     print(array[i][0])
    
# BOJ - Silver 18310
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# # avg = int(sum(data) / n) # 평균 X, 중앙값 사용해야 함
# mid = 0
# if n % 2 == 0:
#     mid = data[int(n / 2) - 1]
# else:
#     mid = data[int(n / 2)]

# print(mid)
