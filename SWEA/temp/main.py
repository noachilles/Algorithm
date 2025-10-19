def rotated_90(a):
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 배열 크기 변화 없음
def rotated_180(a):
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[n - i - 1][m - j - 1] = a[i][j]
    return result

def rotated_270(a):
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = a[i][j]
    return result

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
n = len(a)
m = len(a[0])
# print(rotated_90(a))
# print(rotated_180(a))
# print(rotated_270(a))

# 배열의 특정 부분을 회전시킨다
# (sy, sx)는 회전할 부분 좌측 상단의 좌표 - 정사각형
def small_rotated_90(sy, sx, length):
    global a
    new = [arr[:] for arr in a]
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            # 1단계: 기준 좌표 (sy, sx)를 (0, 0)으로 옮겨준다
            oy, ox = y - sy, x - sx
            # 2단계: 90도 회전했을 때 좌표를 구한다
            # 이건 위의 90도 전체 회전과 동일함
            ry, rx = ox, length - oy - 1
            # 3단계: 다시 (sy, sx)를 더해준다
            new[sy + ry][sx + rx] = a[y][x]

    return new

new = small_rotated_90(1, 1, 2)
# for i in range(n):
#     print(new[i])

# 순열
def permutations(n, new_arr):
    global arr
    # 순서 상관 O, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            # 방문 처리 후 재귀 -> 중복X
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            # 다시 풀어준다
            visited[i] = 0

# 중복 순열
# 가장 라이트하다~
def product(n, new_arr):
    # 순서 O, 중복 O
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

# 조합
def combinations(n, new_arr, start):
    # 순서 X, 중복 X
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(start, len(arr)):
        combinations(n, new_arr + [arr[i]], i+1)

# 중복 조합
def rep_combinations(n, new_arr, start):
    # 순서 X, 중복 O
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(start, len(arr)):
        rep_combinations(n, new_arr + [arr[i]], i)

arr = [1, 2, 3, 4]
visited = [0] * len(arr)
# print('순열')
# permutations(2, [])
# print('중복 순열')
# product(2, [])
# print('조합')
# combinations(2, [], 0)
# print('중복 조합')
# rep_combinations(2, [], 0)

# 중력 - 바닥까지 하강
# 한 칸씩 움직이지는 않는다. 여기서 특정 조건이 붙는 경우가 많다고
def gravity():
    n = len(grid)
    m = len(grid[0])

    # 범위 이유 알아내기 : n-1 줄은 내려갈 곳이 없기 때문에
    for i in range(n-1):
        for j in range(m):
            p = i
            # 현재 칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸씩 연쇄적으로 내려옴
            while 0 <= p and grid[p][j] == 1 and grid[p+1][j] == 0:
                grid[p][j], grid[p+1][j] = grid[p+1][j], grid[p][j]
                p -= 1

grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
for i in range(len(grid)):
    print(grid[i])
gravity()
for i in range(len(grid)):
    print(grid[i])

# 달팽이 배열
# 2차원 배열에서 시작 지점을 기준으로 나선형으로 값에 접근하는 코드 유형

zero_base = [[0] * 5 for _ in range(5)]

# 안에서 밖으로
def tornado(arr):
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y = len(arr) // 2
    x = len(arr) // 2
    num = 0
    dist = 1
    d_idx = 0 # 서 남 동 북 순서
    move_count = 0 # 2가 되면 dist 길이가 1 늘어나고 move_count는 다시 0으로 초기화
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            ny, nx = dy + y, dx + x
            if (ny, nx) == (0, -1):
                return
            num += 1
            arr[ny][nx] = num
            y = ny
            x = nx
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0
    return arr

res = tornado(zero_base)
for i in range(5):
    print(zero_base[i])