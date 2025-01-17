# 이코테 실전문제 4-1

# 입력
# (행의 위치 1~8 + 열의 위치 a~h)
# 출력
# 나이트가 이동 가능한 경우의 수

## 1
p = input()
x,y = ord(p[0]), int(p[1])
res = list()
xmat = [2, 2, -2, -2, 1, 1, -1, -1]
ymat = [1, -1, 1, -1, 2, -2, 2, -2]


for i in range(len(xmat)):
    nx, ny = x, y
    nx += xmat[i]
    ny += ymat[i]
    if nx < ord('a') or nx > ord('h') or ny < 1 or ny > 8:
        continue
    res.append((nx, ny))
print(len(set(res)))

# 나이트가 이동할 수 있는 8가지 방향을 괄호로 묶어 리스트로 저장해두고 사용도 가능