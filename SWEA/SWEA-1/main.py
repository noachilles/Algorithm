from collections import deque

def test_film(grid):
    visited = [[0] * W for _ in range(D)]
    result = [0] * W
    for c in range(W):
        for r in range(D):
            if visited[r][c] == 1:
                continue
            if result[c] == 1:
                continue
            visited[r][c] = 1
            cnt = 1
            que = deque()
            que.append((r, c))
            while que:
                r, c = que.popleft()
                nr, nc = r + 1, c
                if 0 <= nr < D and 0 <= nc < W and visited[nr][nc] == 0 and grid[nr][nc] == grid[r][c]:
                    visited[nr][nc] = 1
                    que.append((nr, nc))
                    cnt += 1
            if cnt >= K:
                result[c] = 1
        if result[c] == 0:
            return False
    return True

def combinations(num, start, D, arr):
    global flag
    if flag == True:
        return
    if len(arr) == num:
        # print(arr)
        if fill_liquid(arr):
            flag = True
        # fill_nums[num].append(arr[:])
        # 여기에서 fill_liquid 들어간다
        return
    for r in range(start, D):
        for type in range(2):
            combinations(num, r+1, D, arr + [(r, type)])

def fill_liquid(group_lst):
    '''
    group_lst: [[(0, 0)], [(0, 1)]] 이런 식
    :return:
    '''
    global W
    global grid
    # [(0, 1), (1, 1)] 이런 식
    new = [arr[:] for arr in grid]
    for item in group_lst:
        r, type = item
        new[r] = [type] * W
    if test_film(new):
        return True
    return False

# 꼭 지우기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # Common Case
    # D, W, K = 6, 8, 3
    # grid = [[0, 0, 1, 0, 1, 0, 0, 1],
    #         [0, 1, 0, 0, 0, 1, 1, 1],
    #         [0, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 0, 0, 0, 1],
    #         [0, 1, 1, 0, 1, 0, 0, 1],
    #         [1, 0, 1, 0, 1, 1, 0, 1]]

    D, W, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(D)]

    fill_nums = dict()
    liquid_types = dict()
    flag = False

    # 약품을 넣지 않고 평가 진행
    # 기준 미달인 열을 불러올 수 있으면 좋겠다
    if test_film(grid):
        print(f'#{test_case} 0')

    else:
        # 약품 투입 횟수 i를 1씩 늘리며 반복
        for num in range(1, K):
            # grid에서 num개만큼 추출하고
            # 약품을 주입한다
            fill_nums.update({num: []})
            # 약품을 주입할 번호 리스트를 생성
            # liquid_types.update({num: []})
            combinations(num, 0, D, [])
        # print(fill_nums)
        # fill_nums가 변화되어서 num에 따라 불러오기만 하면 될 것 같다~
        #     if fill_liquid(fill_nums[num], grid):
        #         print(f'#{test_case} {num}')
        #         flag = True
        #         break
            if flag == True:
                print(f'#{test_case} {num}')
                break
        if not flag:
            print(f'#{test_case} {K}')


        # ///////////////////////////////////////////////////////////////////////////////////
