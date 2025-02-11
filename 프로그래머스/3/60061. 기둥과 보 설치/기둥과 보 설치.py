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
# answer로는 해결할 수 없음 -> 위의 조건을 만족하도록 해야함

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