import copy

# 모든 경우를 다 살펴보고 -> 그래도 안 되면? 그 때는 False
# 또, key의 1 개수 < lock의 0 개수: False

# 시계방향 회전
def rotate(key):
    m = len(key)
    temp_key = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            temp_key[c][m - 1 -r] = key[r][c]
    return temp_key
    
def check(temp_lock):
    n = len(temp_lock) // 3
    for r in range(n, 2 * n):
        for c in range(n, 2 * n):
            if temp_lock[r][c] != 1:
                return False
    return True
    
def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)

    temp_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for r in range(n):
        for c in range(n):
            temp_lock[r + n][c + n] = lock[r][c]
    for rotation in range(4):
        key = rotate(key)
        for x in range(n * 2):
            for y in range(n * 2): 
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        temp_lock[x + i][y + j] += key[i][j]
                if check(temp_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        temp_lock[x + i][y + j] -= key[i][j]
    return False