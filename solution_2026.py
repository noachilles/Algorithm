# # SWEA - 숫자 만들기
# '''
# N개의 숫자가 적혀 있는 게임 판이 있음
# +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣어
# 수식 계산할 때는 연산자 우선순위는 고려 X, 왼 -> 오 차례대로 계산
# 즉, 1+2*3의 결과는 9

# 주어진 연산자 카드를 사용해 수식 계산 시, 결과가 최대가 되는 수식과 최소가 되는 수식 찾고, 두 값의 차이 구함
# '''

# def get_max_min(cnt, operators, crt_res):
#     global min_res, max_res
#     '''
#     :param cnt: 현재 연산자 개수
#     :param operators: 현재 operators
#     :param crt_res: 현재까지의 연산 결과
#     '''
#     if cnt >= N-1:
#         # print(f'cnt: {cnt}, crt_res: {crt_res}\noperators: {operators}')
#         if crt_res < min_res:
#             min_res = crt_res
#         if crt_res > max_res:
#             max_res = crt_res
#         return
    
#     # operator를 for문으로 반복해서 돌림
#     # 만약 1번 항목 보고 -> 2번 항목 보고 -> 3번까지 보면 다시 돌아감
#     # -> 2번 보던 시점으로 돌아가야 함
#     for op in range(4):
#         if operators[op] > 0:
#             # 매번 시점마다 빼고 더하기
#             cnt += 1
#             operators[op] -= 1
#             if op == 0:
#                 nxt_res =  crt_res + numbers[cnt]
#             elif op == 1:
#                 nxt_res = crt_res - numbers[cnt]
#             elif op == 2:
#                 nxt_res = crt_res * numbers[cnt]
#             else:
#                 nxt_res = int(crt_res / numbers[cnt])
#             get_max_min(cnt, operators, nxt_res)
#             operators[op] += 1
#             cnt -= 1
            

# T = int(input())
# for t in range(1, T+1):
#     min_res = 100000001
#     max_res = -100000001
#     # 숫자의 개수 N
#     N = int(input())
#     # +, -, *, / 순서대로 연산자 카드 개수
#     operators = list(map(int, input().split()))
#     # 수식에 들어가는 N 개의 숫자
#     numbers = list(map(int, input().split()))[:N]
#     '''
#     0.
#     숫자 사이에 연산자를 하나씩 넣어보고, 연산을 진행해야 함
#     연산자를 모두 사용한 시점에, 연산 후 결과 도출
#     그럼 + 하나 쓴 세계 -> + 둘 쓰는 세계 / + 하나, - 하나 쓰는 세계
#     이렇게 이어져야 하므로 DFS로 풀이함
    
#     1.
#     + 하나 쓰고, 그 다음 거에 순서대로 넣고 ... 연산자 개수를 하나씩 줄이면서 0으로 만들기
#     만약 모든 연산자를 사용했다면 -> 어떻게 판단할까?: 횟수로 -> 모든 연산자 사용하면 N-1회차가 되지 않나?
#     N-2가 됨(0부터 시작할 경우에) -> N-1이 되면 연산 후 갱신 
#     연산 후 결과를 현재 최대/최소와 비교해서 갱신
#     '''
#     get_max_min(0, operators, numbers[0])

#     # 결과
#     res = max_res - min_res
#     print(f'#{t} {res}')

# PRO - 단어암기장
'''
# 0
init
- 각 tc 처음에 호출됨
- 크기가 N*M인 암기장 주어짐
- N 최대 20,000 / M 최대 1,000

writeWord(mId, mLen)
- ID가 mId이고, 길이가 mLen인 단어가 주어지면
- 위 규칙에 맞게 암기장에 쓴 후 쓰여진 위치의 "행 번호"를 반환함
- 암기장에 주어진 단어를 쓸 수 없다면, -1을 반환함
- ID값은 1부터 시작해 함수가 호출될 때마다 1씩 증가 => 함수 호출 될 때마다 1씩 증가하네~

eraseWord(mId)
- ID값이 mId인 단어를 암기장에서 지움
- 지우기 전 적힌 위치의 행 번호를 반환함
- 이미 지워졌거나, 적힌 적이 없는 단어의 ID가 주어지면 -1 반환
'''

'''
# 1
- 매번 0행부터, 0열부터 조회해야 할까?
- 행별로 빈칸 개수와 길이를 저장해두면 되는 거 아닐까?
    - 개별로 저장해둘 것인가? : 한다면 시작 열 번호, 길이
    - 조회가 빠른 쪽은? dictionary 빈칸 1: 필요 없음 2 ~ M
    - 'key: 길이 value: 시작 인덱스의 트리? - 최솟값만 뽑으면 되니까'
    - 추가로, min heap의 pop 시간복잡도는 O(1)이라고~~
    - 물론ㅠ 이걸 위해서는 O(logN)의 삽입이 필요함


# 2
- 이상한 점: 한 행에 적혀있는 단어 최대 개수가 60개 이하임을 보장
    - 왜? ... 길이가 2인 단어만 있다면 500개도 넣을 수 있을텐데
    - 이상하다... -> 진짜 모르겠네 이걸 왜 보장해주나?
    - 60개가 넘어가면 시간복잡도가 급격히 커지는, 그런 자료구조가 있나?
=> 칸 단위가 아니라 단어 단위로 보면 시간복잡도가 커지는 구간이 생김
    -> 최대 시간을 막아줌
    
# 3
- writeWord 시뮬레이션
- 단어가 하나 들어옴 -> 빈 공간에 넣어봄
- 다음 단어가 들어옴 -> 0행부터 빈 공간을 찾아봄
- 만약 특정 행에 대한 빈 공간이 없을 경우, 다음 행으로 넘어감

# 4
- eraseWord 시뮬레이션
- ID를 입력받음
- 암기장에 있는 값인지, 아니면 없는 값인지 확인함 <- 중복은 없을 테니까 set으로 관리해도 될 것 같고
- 근데, 만약 더 큰 값이 들어있다면 에러가 발생할 거임
    => 그냥 55000의 index를 가진 list를 생성하고, 값을 t/f로 저장 - 1, 2, 3, 4, 5
- 그럼 위치는 따로 저장해두고 -> t/f로 조회했을 때 f이면 패스 / t이면 위치 조회
- 그리고 비워줘야하니까 길이도 저장해둬야 함
- 그러면 -> eraser를 위해서는
    1. 현재 단어암기장에 존재하는 ID 목록 - 
    2. 현재 단어암기장에 존재하는 ID별 시작 인덱스
    3. 현재 단어암기장에 존재하는 ID별 단어 길이
    이렇게.
    1따로 2, 3 같이 이렇게 저장해두면 쓰기 편할듯 (별도의 dict)
    -> 1 따로 할 필요가 있을까?

# 5
- 시간복잡도
- writeWord를 실행 해
- 각 행 별로 조회를 해(최대 20,000) * 50,000 => 10억
    - 넣을 수 있으면 값을 넣어.. -> ID 목록에 true -> O(1)
    - 시작 인덱스랑 단어 길이도 적어줌 -> O(1)
- 아니면, 길이별로: 최소 인덱스를 저장해두면 어떨까?
    - 관리 방법이 잘 떠오르지 않음
- 아니면, 행별로 저장하되, 길이별로도 저장해두면 어떨까?

# 6
시뮬레이션
- N = 5, M = 5
- 행별 길이 저장소 {0: {5: {0}})} # {행: {길이: 시작인덱스}}
- writeWord(1, 3)
- 행별 길이 저장소 {0: {5: {-1}, 2: {3}}} # {행: {길이: 시작인덱스}}
- 한 가지 간과한 점: 단어의 길이보다 긴 공간에는 해당 단어를 기록할 수 있음

- 판단해야 하는 것 - 길이! 넣을 수 있다 없다를 판단해야 함

=> 세그먼트 트리를 사용해야 할 것 같음
1. 각 행별로 max 빈칸 길이를 저장
2. min 
=> 세그먼트 트리
'''

# 26-01-26
'''
모든 벌꿀을 살피면서, 값이 최대가 되는 경우를 찾자 -> 일단 전체 탐색
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, M, C = map(int, input().split())
    
#     grid = []
#     for i in range(N):
#         row = list(map(int, input().split()))
#         grid.append(row)
#     print(grid)

    # N-1만큼 돌면 됨 -> 다른 것도!!!

# def solution(sizes):
#     mi, ma = 1, 1
#     for r, c in sizes:
#         if r < c:
#             if mi < r:
#                 mi = r
#             if ma < c:
#                 ma = c
#         elif c < r:
#             if mi < c:
#                 mi = c
#             if ma < r:
#                 ma = r
#         else:
#             if mi < c:
#                 mi = c
#             if ma < r:
#                 ma = r
#     answer = mi * ma
#     return answer

# 26-07-19
# def solution(answers):
#     N = 5
#     L = len(answers)

#     first = [i for i in range(1, N+1)]
#     second = []
#     for i in (1, 3, 4, 5):
#         second += [2]
#         second += [i]
#     third = []
#     for i in (3, 1, 2, 4, 5):
#         third += [i] * 2
    
#     L_f = len(first)
#     L_s = len(second)
#     L_t = len(third)

#     scores = [0, 0, 0]

#     for i in range(L):
#         if answers[i] == first[i%L_f]:
#             scores[0] += 1
#         if answers[i] == second[i%L_s]:
#             scores[1] += 1
#         if answers[i] == third[i%L_t]:
#             scores[2] += 1
    
#     answer = []
#     maximum = 0
#     for i in range(3):
#         if scores[i] > maximum:
#             maximum = scores[i]
    
#     for j in range(3):
#         if scores[j] == maximum:
#             answer.append(j+1)

#     return answer

# from itertools import permutations
#
# def solution(numbers):
#     L = len(numbers)
#     answer = 0
#     visited = set()
#     # 1. 모든 조합으로 수를 만들어야 함
#     # 1) 조합으로 문자열을 만들어야 함
#     for i in range(1, L+1):
#         combinations_list = []
#         for comb in permutations(numbers, i):
#             # 2) 문자열을 수로 만들어야 함
#             num = int("".join(map(str, comb)))
#             if num not in visited:
#                 combinations_list.append(num)
#                 visited.add(num)
#         # 2. 각 조합의 수에 대한 소수 판별이 필요함
#         for number in combinations_list:
#             # 1) 일단 1이 아니어야 함
#             if number <= 1:
#                 continue
#             # 2) 1 말고는 나누어지는 수가 없어야 함
#             else:
#                 flag = True
#                 for j in range(2, number):
#                     if number % j == 0:
#                         flag = False
#                         break
#                 if flag:
#                     answer += 1
#     return answer
#
# if __name__ == '__main__':
#     print(solution("011"))

'''
# 정올 - 4520 햄버거 분배
# (사람 - 햄버거) 거리 <= k : 섭취 가능
# - 최대 5명이 햄버거 섭취 가능
# 배열을 왼쪽부터 오른쪽으로 훑으며, 사람을 먼저 발견
# 가장 아쉬운 햄버거부터 먹자!
# 맨 처음 발견된 사람 입장에서는: 탐색범위(현재 위치 - k, 현재 위치 + k)
# 왜? 내 왼쪽 햄버거는 내가 먹지 않으면, 나보다 오른쪽 사람들은 먹을 수 없음
# input
n, k = map(int, input().split())
table = input()
eaten = set()
result = 0

for i in range(n):
    # 사람을 발견하면
    if table[i] == 'P':
        # 사람의 왼쪽 끝 ~ 오른쪽 끝까지 탐색
        for j in range(i-k, i+k+1):
            if j < 0 or j >= n:
                continue
            # 햄버거를 발견하면
            if table[j] == 'H' and j not in eaten:
                # 1. 햄버거 먹었음을 표시
                eaten.add(j)
                # 2. result 1 증가
                result += 1
                # 3. 햄버거 하나 먹었으므로 탐색 X, break
                break

print(result)
'''

# # 정올 1695 단지번호붙이기
# # 1은 집이 있음 / 0은 집이 없음
# # 연결된 집들의 모임인 단지를 정의 / 단지에 번호
# # 집이 연결됨: 좌우, 아래위로 다른 집이 있는 경우
#
# n = int(input())
# grid = []
# for Y in range(n):
#     grid.append(list(map(int, str.strip(input()))))
#
# directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# # 각 단지별 집의 개수를 오름차순 저장할 우선순위 큐
# import heapq
# group = 0
# numbers = []
# visited = [[0] * n for _ in range(n)]
#
# def dfs(y, x):
#     # 1 depth 들어왔음을 표시
#     number = 1
#     for d in range(4):
#         ny, nx = y + directions[d][0], x + directions[d][1]
#         if 0 <= ny < n and 0 <= nx < n:
#             if grid[ny][nx] == 1 and not visited[ny][nx]:
#                 visited[ny][nx] = 1
#                 # dfs 빠져나오면서 적어도 1 depth 들어갔다 나옴
#                 number += dfs(ny, nx)
#     return number
#
# # 맨 왼쪽 위부터 우측 아래로
# for y in range(n):
#     for x in range(n):
#         if grid[y][x] == 1 and visited[y][x] == 0:
#             group += 1
#             visited[y][x] = 1
#             heapq.heappush(numbers, dfs(y, x))
# print(group)
# for i in range(group):
#     print(heapq.heappop(numbers))

# 정올 - 1335 색종이 만들기
# 주어진 종이를 일정한 규칙에 따라 잘라서, 다양한 크기를 가진 정사각형 모양의 하얀색, 파란색 색종이
# 하얀색 색종이와 파란색 색종이 개수
# 만약 정사각형 내부가 모두 같은 색상이 아니라면, N/2로 가로, 세로를 자름
# N은 (2, 4, 8, 16, 64, 128 중 하나)

# 분할정복 - 큰 문제를 풀기 위해서 그 문제를 작은 문제로 쪼개는 것
# 처음에는 N에서부터 시작
# 2^0 까지...
# // 2를 해서, 다음 함수로 들어감
# 전수조사 -> 만약 발견되면 다음으로
# 발견 안 되면 돌아옴
# 현재 범위의 작은 범위를 찾을 수 있도록 유도해야 함
# N = int(input())
# grid = []
# for Y in range(N):
#     grid.append(list(map(int, input().split())))
#
# blue = 0
# white = 0
#
# def search(v, sr, sc, n):
#     global blue, white
#     flag = True
#     # 만약 N이 1이면 1을 반환하고 종료
#     if N == 1:
#         if v == 0:
#             white += 1
#         else:
#             blue += 1
#         return
#
#     # v는 값이고 r, c는 좌표
#     # 반복하면서 -> 탐색 후 값이 다른 것이 있다면 depth 추가
#     for r in range(sr, sr + n):
#         for c in range(sc, sc + n):
#             if grid[r][c] != v:
#                 flag = False
#                 dist = n//2
#                 search(grid[sr][sc], sr, sc, dist)  # 2사분면
#                 search(grid[sr+dist][sc], sr+dist, sc, dist)   # 3사분면
#                 search(grid[sr][sc+dist], sr, sc+dist, dist)   # 1사분면
#                 search(grid[sr+dist][sc+dist], sr+dist, sc+dist, dist)  # 4사분면
#                 return
#     if flag:
#         if v == 0:
#             white += 1
#         else:
#             blue += 1
#     return
#
# search(grid[0][0], 0, 0, N)
# print(white)
# print(blue)

# 정올 1370 회의실 배정

# import heapq
#
# N = int(input())
# q = []
# last_end_time = 0
# meeting_numbers = 0
# results = []
#
# for i in range(N):
#     num, start, end = map(int, input().split())
#     heapq.heappush(q, (end, start, num))
#
# while q:
#     end, start, num = heapq.heappop(q)
#     # 만약 이미 회의가 있는 시간대라면
#     if start >= last_end_time:
#         results.append(num)
#         meeting_numbers += 1
#         last_end_time = end
#     else:
#         continue
#
# print(meeting_numbers)
# print(*results)

# 정올 5170 나무꾼 미르코
# M미터 이상의 나무를 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
# 나무의 수 N, 벌목해야 하는 나무 길이 최솟값 M

# 절단기 높이를 result로 둔다
# 이진탐색 -> for문 돌며 1씩 뺌
# 이진탐색: logN, for문: N

# 만약 제일 높은 나무에 대해서
# 이진탐색 수행 -> for문에서 key값을 빼봄
# 만약 만족하면 -> OK
# 만약 만족하지 않으면: 부족하면 큰쪽 / 넘치면 많은쪽
# 넘치는 건 저장해두고, 만약 다음 턴에서 부족해지면 -> 최신값 반환
# result = 0
#
# def binary_search(start, end):
#     global M, result
#     if end <= start:
#         return
#     key = (end + start) // 2
#     get = 0
#     for tree in trees:
#         get += max(tree - key, 0)
#     if get > M:
#         result = key
#         binary_search(key+1, end)
#     elif get < M:
#         binary_search(start, key)
#     else:
#         result = key
#         return
#
# N, M = map(int, input().split())
# trees = list(map(int, input().split()))
#
# trees.sort()
# highest = trees[-1]
# binary_search(0, highest)
# print(result)

# 1078 저글링 방사능 오염
from collections import deque

# 구하는 것1: 최소 몇 초가 걸리는지 - 사망까지 3초
result = 0
# 구하는 것2: 남아있는 저글링 수
numbers = 0

# 입력
M, N = map(int, input().split())
grid = []
for r in range(N):
    grid.append(list(map(int, input().strip())))
# 1은 저글링 O, 0은 저글링 X
# 방사능 오염 가하는 위치가 열, 행(x, y)순
# x, y 좌표의 시작은 1
x, y = map(int, input().split())
x -= 1
y -= 1

for r in range(N):
    for c in range(M):
        if grid[r][c]:
           numbers += 1

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# bfs로 저글링들에게 하나씩 감염을 시킴
# 처음 시작은 3부터 하고, 마지막 업데이트를 결과로 반환
# 시작점 세팅
q = deque()
q.append((y, x, 3))
visited = [[0] * M for _ in range(N)]
visited[y][x] = 1
numbers -= 1

while q:
    cy, cx, time = q.popleft()
    result = time
    for d in range(4):
        ny, nx = cy + directions[d][0], cx + directions[d][1]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if visited[ny][nx] == 0 and grid[ny][nx]:
            visited[ny][nx] = 1
            numbers -= 1
            # 1을 더함
            q.append((ny, nx, time+1))
# ---
print(result)
print(numbers)