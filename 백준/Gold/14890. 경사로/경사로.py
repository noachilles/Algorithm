# 한 줄씩 살펴 본다
def cnt_road():
    global arr, cnt
    for i in range(N):
        visited = [0] * N
        chk = True
        for j in range(N-1):
            diff = arr[i][j] - arr[i][j+1]
            # 높낮이와 상관 없이 높이 차가 2이상이라면
            # 다음 줄을 확인한다
            if diff < -1 or diff > 1:
                chk = False
                break
            # 앞이 더 높다면
            elif diff == 1:
                # 경사로 설치 확인, 방향 1(x+1, y)
                if not chk_ramp(visited, j+1, i, diff):
                    chk = False
                    break
            # 뒤가 더 높다면
            elif diff == -1:
                # 경사로 설치 확인, 방향 -1(x-1, y)
                if not chk_ramp(visited, j, i, diff):
                    chk = False
                    break
        # 모두 끝나면
        if chk:
            cnt += 1
    
# 경사로 설치 함수
def chk_ramp(visited, x, y, d):
    global L
    stack = []
    if d == 1:
        for i in range(0, L):
            if ((x+i) < 0 or (x+i) >= N) or visited[x+i]:
                return False
            else:
                stack.append(x+i)
            
    else:
        for i in range(0, L):
            if ((x-i) < 0 or (x-i) >= N) or visited[x-i]:
                return False
            else:
                stack.append(x-i)
    for k in stack:
        visited[k] = 1
    return True

if __name__ == "__main__":
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    cnt_road()
    arr = [list(arr[::-1][i][j] for i in range(N)) for j in range(N)]
    cnt_road()
    print(cnt)