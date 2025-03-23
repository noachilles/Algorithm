from collections import deque


def Rf():
    global A, R, mx_c
    new_A = []
    for i in range(R):
        d = dict()
        deq = deque()
        deq.clear()
        deq.extend(A[i])
        while deq:
            # popleft 하면서 개수 세기
            key = deq.popleft()
            if key == 0: continue
            if key in d:
                d[key] += 1
            else:
                d.update({key: 1})
        temp = sorted(d, key = lambda x: (d[x],x))
        new_R = []
        for val in temp:
            new_R.append(val)
            new_R.append(d[val])
        mx_c = max(mx_c, len(new_R))
        new_A.append(new_R)
    for i in range(len(new_A)):
        new_A[i] += [0] * (mx_c - len(new_A[i]))
    A = [arr[:] for arr in new_A]

def Cf():
    global A, C, mx_r
    new_A = []
    # C연산 - 배열 A의 모든 열에 대해 수행
    for j in range(C):
        d = dict()
        deq = deque()
        deq.clear()
        deq.extend(arr[j] for arr in A[:])
        while deq:
            key = deq.popleft()
            if key == 0: continue
            if key in d:
                d[key] += 1
            else:
                d.update({key: 1})
        temp = sorted(d, key=lambda x: (d[x], x))
        new_C = []
        for val in temp:
            new_C.append(val)
            new_C.append(d[val])
        mx_r = max(mx_r, len(new_C))
        new_A.append(new_C)
    for i in range(len(new_A)):
        new_A[i] += [0] * (mx_r - len(new_A[i]))
    new_A = list(map(list, zip(*new_A)))
    A = [arr[:] for arr in new_A]
    
# 100개 이상이 되면 자르기
def cut(n):
    # 만약 행이 100개 이상이라면 행을 자르기
    if n > 0:
        A = A[:100]
    # 만약 열이 100개 이상이라면
    else:
        for i in range(R):
            A[i] = A[i][:100]

R, C = 3, 3
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
# R연산 - 배열 A의 모든 행에 대해 정렬 수행
mx_r = 0
mx_c = 0
for t in range(101):
    if 0 <= r-1 < R and 0 <= c-1 < C:
        if A[r-1][c-1] == k:
            print(t)
            exit(0)
    if R >= C:
        Rf()
        if mx_c > 100:
            cut(-1)
            mx_c = 100
        C = mx_c
    else:
        Cf()
        if mx_r > 100:
            cut(1)
            mx_r = 100
        R = mx_r
print(-1)