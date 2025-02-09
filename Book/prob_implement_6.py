from collections import deque
# check 함수까지 모두 만들고 나서야 이상함을 감지함
# check 함수를 통해 불가능/가능을 판단하는 것까지는 좋았음
# 하지만 이걸로 판단하기에는 되돌릴 수 없음.. 매번 모든 것을 확인하는 것이 좋을 것 같음 -> 그래프에 값을 저장하지 않고.
# 지금은 순서대로 할 수밖에 없어서 '제거' 기능이 정상 작동하지 않음
# 나중에 함수를 다시 만들어서 해보자

def check(n, c, r, a, wall):
    if a == 0:
        if r == n or wall[r][c] != 0:
            return True
        else:
            return False
    else:
        if wall[r][c] == 1 or wall[r][c+1] == 1 or wall[r][c] == 3 or wall[r][c+1] == 3:
            return True
        elif c + 2 <= n and wall[r][c] == 2:
            if wall[r][c+2] == 2:
                return True
        else:
            return False
    return True
        
def solution(n, build_frame):
    answer = []
    # 1000개 정도의 입력이 있으니 모든 상황을 다 생각해보면 된다
    q = deque(build_frame)
    wall = [[0] * (n + 1) for _ in range(n + 1)]
    while q:
        c, r, a, b = q.popleft()
        r = (n - r)
        # 기둥을 설치할 경우
        if a == 0 and b == 1:
            if check(n, c, r, a, wall):
                if wall[r-1][c] == 2:
                    wall[r-1][c] = 3
                else:
                    wall[r-1][c] = 1
                answer.append([c, n-r, a])
            else:
                continue
        # 보를 설치할 경우
        elif a == 1 and b == 1:
            if check(n, c, r, a, wall):
                if wall[r][c+1] == 1:
                    wall[r][c+1] = 3
                else:
                    wall[r][c+1] = 2
                answer.append([c, n-r, a])
            else:
                continue
        else:
            if a == 0:
                wall[r-1][c] -= 1
            else:
                wall[r][c+1] -= 2
                answer.remove([c, n-r, a])
                for k in range(len(answer)):
                    j, i, x = answer[k]
                    i = n - i
                    print(check(n, j, i, x, wall), (n-i, j, x))
                    if check(n, j, i, x, wall) == False:
                        answer.append([c, n-r, a])
        answer.sort()
    return answer