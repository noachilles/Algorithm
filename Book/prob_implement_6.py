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

# solution 2. 실패
# 설치 유효 검사는 쉬움 - 문제 조건에서 하라는 걸 하나씩 추가하면 됨
# 해당 부속품의 좌표를 (x, y)라 한다면
# 기둥
# 기둥에 영향을 받는 것은
    # 바로 위 기둥(x, y + 1)
    # 바로 위 보(x, y + 1)
    # 오른쪽으로 걸쳐서 얹어진 보(x - 1, y + 1)
# 보
# 보를 빼면 영향을 받는 것은
    # 바로 위 기둥(x, y + 1)
    # 오른쪽 위 기둥(x + 1, y + 1)
    # 오른쪽 보(x + 1, y)
    # 왼쪽 보(x - 1, y)
# 위 좌식들에 대해 유효성 검사를 수행하면 된다~
# 코드를 짜면서 느끼는 점: 역시 중요한 건
# 회복탄성력이다 **

from collections import deque

def check(n, command, wall):
    c, r, a = command
    r = n - r
    # 기둥일 때
    if a == 0:
        # 기둥을 없애고
        wall[r - 1][c] -= 1
        if wall[r-2][c] == 1:
            # r = n-r
            return draw(n, [c, n-(r-1), 0], wall)
        elif wall[r-1][c] == 2:
            # r = n-r
            return draw(n, [c-1, n-(r-1), 1], wall)
        elif wall[r-1][c+1] == 2:
            # r = n-r
            return draw(n, [c, n-(r-1), 1], wall)
    else:
        wall[r][c + 1] -= 2
        if wall[r-1][c] == 1:
            # r = n-r
            return draw(n, [c, n-(r-1), 0], wall)
        elif wall[r-1][c+1] == 1:
            # r = n-r
            return draw(n, [c+1, n-(r-1), 0], wall)
        elif wall[r][c+2] == 2:
            # r = n-r
            return draw(n, [c+2, n-r, 1], wall)
        elif wall[r][c] == 2:
            # r = n-r
            return draw(n, [c, n-r, 1], wall)
    return True
        

def draw(n, command, wall):
    c, r, a = command
    r = n - r 
    if a == 0:
        # 바닥이면
        if r == n:
            return True
        # 아래에 보 혹은 기둥이 있다면
        elif wall[r][c] > 0:
            return True
        return False
    # 보에 대해
    else:
        if c > n - 1:
            return False
        # 왼쪽 끝이 기둥 위라면
        elif wall[r][c] == 1 or wall[r][c] == 3:
            return True
        # 오른쪽 끝이 기둥 위라면
        elif wall[r][c + 1] == 1:
            return True
        elif wall[r][c] >= 2 and wall[r][c + 2] >= 2:
            print(f'check {c}, {r}, {a}')
            return True
        return False
        

def solution(n, build_frame):
    answer = []
    wall = [[0] * (n + 1) for _ in range(n + 1)]
    q = deque(build_frame)
    while q:
        c, r, a, b = q.popleft()
        if b == 1:
            answer.append([c, r, a])
            if draw(n, [c, r, a], wall):
                r = n - r
                if a == 0:
                    wall[r-1][c] += 1
                else:
                    wall[r][c+1] += 2
                continue
            else:
                answer.remove([c, r, a])
        else:
            print('remove: ', c, r, a)
            answer.remove([c, r, a])
            # 여기에서는 필요한 것만 체크해야 함
            if check(n, [c, r, a], wall):
                continue
            else:
                answer.append([c, r, a])
    answer.sort()
    
    return answer

# 그래프를 만들지 않고 그냥 해결할 수 있도록 하자
# solution 3. -> 여전히 똑같음

from collections import deque

def possible(command, answer):
    x, y, stuff = command
    # print('possible: ', command)
    if stuff == 0:
        # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
        if y == 0 or [x-1, y, 1] in answer or [x, y-1, 0] in answer or [x, y, 1] in answer:
            return True
        return False
    elif stuff == 1:
        # 한쪽 끝 부분이 기둥 위 or 다른 보 두 개와 연결
        if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
            return True 
        elif ([x-1, y, 1] in answer) and ([x+1, y, 1] in answer):
            return True
        return False

def remove_possible(command, answer):
    x, y, stuff = command
    # print('remove: ', command)
    res = [True]
    if stuff == 0:
        # 바로 위 기둥
        if [x, y+1, 0] in answer:
            res.append(possible([x, y+1, 0], answer))
        # 바로 위 보
        if [x, y+1, 1] in answer:
            res.append(possible([x, y+1, 1], answer))
        # 오른쪽으로 걸쳐서 얹어진 보
        if [x-1, y+1, 1] in answer:
            res.append(possible([x-1, y+1, 1], answer))
        # 셋 다 없으면 삭제 가능
    if stuff == 1:
        # 바로 위 기둥
        if [x, y, 0] in answer:
            res.append(possible([x, y, 0], answer))
        # 오른쪽 위 기둥
        if [x+1, y, 0] in answer:
            res.append(possible([x+1, y, 0], answer))
        # 오른쪽 보
        if [x+1, y, 1] in answer:
            res.append(possible([x+1, y, 1], answer))
        # 왼쪽 보
        if [x-1, y, 1] in answer:
            res.append(possible([x-1, y, 1], answer))
        # 모두 없으면 삭제 가능
    if False in res:
        return False
    return True
            

def solution(n, build_frame):
    answer = []
    q = deque(build_frame)
    while q:
        c, r, a, b = q.popleft()
        if b == 1:
            answer.append([c, r, a])
            if not possible([c, r, a],answer):
                answer.remove([c, r, a])
        else:
            answer.remove([c, r, a])
            if not remove_possible([c, r, a],answer):
                answer.append([c, r, a])
    answer.sort()
    
    return answer