import sys
input = sys.stdin.readline

n = int(input())
array = [[] for _ in range(n)]
for i in range(n):
    data = list(input().split())
    array[i] = [data[0], int(data[1]), int(data[2]), int(data[3])]

array.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(array[i][0])