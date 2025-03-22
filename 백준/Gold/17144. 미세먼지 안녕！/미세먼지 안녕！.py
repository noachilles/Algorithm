from collections import deque
def spread():
    # 미세먼지 확산
    global cleaned, purifier_r
    for r in range(R):
        for c in range(C):
            if room[r][c] == -1:
                # 회전을 위해 r값을 저장해둔다
                purifier_r = min(purifier_r, r)
            if room[r][c] >= 5:
                value = room[r][c]//5
                # 확산된 방의 개수 
                cnt = 0
                # 확산
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C:
                        if cleaned[nr][nc] != -1:
                            cleaned[nr][nc] += value
                            cnt += 1
                cleaned[r][c] -= value * cnt
            
# 공청기를 돌린다
# p는 공기청정기 r, end는 각 방향의 끝(위쪽 공청기는 end가 0, 아래는 R-1)
# d는 방향 아래가 +1, 위가 -1
def purify(p, end, d):
    global cleaned
    deq = deque()
    if p > end:
        deq.extend(arr[0] for arr in cleaned[end-d:p][::-1]) # 왼쪽
    else:
        deq.extend(arr[0] for arr in cleaned[p+d:end])
    deq.extend(cleaned[end]) # 위쪽
    if p > end:
        deq.extend(arr[C-1] for arr in cleaned[end-d:p])
    else:
        deq.extend(arr[C-1] for arr in cleaned[p+d:end][::-1]) # 오른쪽
    deq.extend(cleaned[p][1:][::-1])
    deq.append(0) # 정화된 공기 하나 추가
    deq.popleft()
    
    for i in range(p+d, end, d):
        cleaned[i][0] = deq.popleft()
    for j in range(0, C):
        cleaned[end][j] = deq.popleft()
    for i in range(end-d, p, -d):
        cleaned[i][C-1] = deq.popleft()
    for j in range(C-1, 0, -1):
        cleaned[p][j] = deq.popleft()

def cnt_dirt():
    global room
    cnt = 0
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                cnt += room[r][c]
    return cnt

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

cleaned = [arr[:] for arr in room]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
purifier_r = R

for i in range(T):
    
    spread()
    purify(purifier_r, 0, -1)
    purify(purifier_r+1, R-1, +1)
    room = [arr[:] for arr in cleaned]
print(cnt_dirt())