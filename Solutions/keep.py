# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# # zip
# # 시계 방향 90
# # print(list(zip(*arr[::-1])))
# arr_90 = list(map(list, zip(*arr[::-1])))
# # print(arr_90)
# arr_180 = [a[::-1] for a in arr[::-1]] # 역방향의 역방향
# print(arr_180)

# arr_270 = list(map(list,zip(*[a[::-1] for a in arr])))
# # 혹은
# arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
# # print(arr_270)

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
# 시계 방향 90
new_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_90[j][n - i - 1] = arr[i][j]
# print(new_90)

# 시계 180
new_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n - i - 1][n - j - 1] = arr[i][j]
# print(new_180)

new_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_270[n - 1 - j][i] = arr[i][j]
# print(new_270)

def rotated_90(a):
    m = len(a)
    n = len(a[0])
    result = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m-i-1] = a[i][j]
    return result

def rotated_180(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[n - i - 1][m - j - 1] = a[i][j]
    return result

def rotated_270(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = a[i][j]
    return result

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(rotated_90(a))
# print(rotated_180(a))
# print(rotated_270(a))

# 부분 회전
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sy, sx = 2, 2
length = 3

def rotate_90(sy, sx, length):
    global arr, new_arr
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            oy, ox = y - sy, x - sx
            # 90도 회전했을 때 좌표
            ry, rx = ox, length - oy - 1
            # 다시 sy, sx 더해주기
            new_arr[sy + ry][sx + rx] = arr[y][x]
    
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            arr[y][x] = new_arr[y][x]
            print(arr[y][x])

rotate_90(sy, sx, length)

# for i in range(len(arr)):
#     print(arr[i])

