# 1.
# 토끼들이 점수를 건 경주를 진행함
# P마리의 토끼가 N x M 크기의 격자 위에서 경주 진행 준비
# 토끼에게는 고유한 번호가 붙어있음
# 이동해야 하는 거리도 정해져 있음
# i번 토끼의 고유번호는 pid_i, 이동해야 하는 거리는 d_i
# 처음 토끼들은 전부 (1행, 1열)에 있음

# 3.
# 고유번호가 pid_t인 토끼의 이동거리를 L배 해줌
# 계산 도중 특정 토끼의 이동거리가 10^9을 넘어가는 일은 발생X

# 4.
# 각 토끼가 모든 경주를 진행하며 얻은 점수 중 가장 높은 "점수" 출력

import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq

# 토끼 정보가 저장된 dictionary
# pid_i: (d_i, 1, 1) 초기화
rabbits_info = dict()
# 토끼들의 점수
rabbits_score = dict()
# 토끼들의 전체 점수
total_sum = 0
N, M, P = 0, 0, 0

# 순서 별로 중요하지 않음 - 부딪혀서 반대 방향으로 갈 수도 있기 때문에
# 어차피 4번 다 돌아야 함
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def init(command):
    """
    100일 때, 경주 시작 준비

    토끼는 고유번호와 이동해야 하는 거리 정보가 저장되어야
    위치도 함께 저장해야 함 -> 이동을 해야하므로
    """
    global N, M, P
    # 전체 명령 길이
    N, M, P = map(int, command[1:4])
    # 명령어로부터 토끼의 고유번호, 이동 거리를 저장
    p = 0
    while p < P:
        idx = 4 + (p * 2)
        # 고유번호, 거리
        pid_i, d_i = map(int, command[idx:idx+2])
        rabbits_info[pid_i] = (d_i, 1, 1)
        # 점수 초기화
        rabbits_score[pid_i] = 0
        p += 1

# 2.
# K번 반복
    # 우선순위가 높은 토끼를 뽑아 멀리 보내줌
    # 우선순위는 순서대로
    # 1. 현재까지의 총 점프 횟수가 적은 토끼
    # 2. 현재 서있는 행 번호 + 열 번호가 작은 토끼
    # 3. 행 번호가 작은 토끼
    # 4. 열 번호가 작은 토끼
    # 5. 고유번호가 작은 토끼
    '''
    여러 개의 키를 기준으로 하는, heap을 구현해야 할까?
    '''

    # 상하좌우 네 방향으로 각각 d_i만큼 이동했을 때의 위치를 구함
    # 이동하는 도중 그 다음 칸이 격자를 벗어나면, 반대 방향 한 칸
    # 4개의 위치 중
    # 행 번호 + 열 번호가 큰 칸
    # 행 번호가 큰 칸
    # 열 번호가 큰 칸
    # 이동한 칸이 (r_i, c_i)라 했을 때, i번 토끼 제외한 나머지: r_i + c_i 점수

# K번의 턴 동안 한 번이라도 뽑혔던 적이 있던 토끼 중 우선순위 높은 토끼에게 점수 S를 더해줌
# 1. 현재 서있는 행 번호 + 열 번호가 큰 토끼
# 2. 행 번호가 큰 토끼
# 3. 열 번호가 큰 토끼
# 4. 고유번호가 큰 토끼

def start_race(command):
    global total_sum
    """
    200 K S
    """
    K, S = map(int, command[1:3])
    # 점프할 토끼 우선순위 위한 heap
    jump_heap = []
    # 최종 점수 추가해줄 토끼 구하기 위한 set
    jumped_rabbits = set()
    best_rabbit_of_round = (-1, -1, -1, -1) # (r+c, r, c, pid)
    # 초기화
    for pid in rabbits_info.keys():
        # (jump_cnt, r+c, r, c, pid)
        d, r, c = rabbits_info[pid]
        heapq.heappush(jump_heap, (0, r+c, r, c, pid, d))
        

    for i in range(K):
        # 우선순위가 높은 토끼를 멀리 보내줌
        now_j, now_rc, now_r, now_c, pid_i, d_i = heapq.heappop(jump_heap)
        # 점프 토끼
        jumped_rabbits.add(pid_i)
        turn_heap = []

        nxt_dir = 0
        nxt_r = 0
        nxt_c = 0
        # 토끼를 4개의 방향으로 이동시킴 - 이동 중에 더 크면 한 칸
        for d in range(4):
            # 이동 중에 범위를 벗어나면, 반대 방향으로 한 칸 이동함
            # (이동 칸 수 - 벽까지 남은 횟수) / M 연산을 수행하고, 그 값의 홀/짝 유무에 따라서 방향을 정함
            # 몫(quo)이 0 or 짝수이면: 기존 방향 & 홀수이면: 반대 방향으로 이동
            # 나머지 rem 값이 적으면, 특정 방향에서 반대 방향으로 rem 칸 이동
            # => 안 됨!
            '''
            해설 참고
            d_i는 d_i % (2 * (N-1)) 또는 d_i % (2 * (M-1)) 으로 줄여서 계산할 수 있음
            이렇게 줄어든 거리만큼만 시뮬레이션!
            '''
            '''
            # 줄어든 거리만큼을 steps라는 변수에 담음
            steps = 0
            # 세로 이동일 경우(행 이동 - N)
            if d % 2 == 0:
                steps = d_i % (2 * (N-1))
            else:
                steps = d_i % (2 * (M-1))
            # 움직인 횟수와 방향을 정함
            # print(steps)
            step_num = 0
            step_d = d
            nr, nc = now_r, now_c
            
            # 직접 모든 경과를 보는 작업
            while step_num < steps:
                tr, tc = nr + directions[step_d][0], nc + directions[step_d][1]

                # 이렇게 한 번을 움직이고 나면,
                # 만약 범위 내에 있다면
                if 1 <= tr <= N and 1 <= tc <= M:
                    # 횟수를 1 증가
                    nr, nc = tr, tc
                    step_num += 1
                # 범위 내에 있지 않다면 - 반대 방향으로 움직여야 함
                # 방향만 바꿔주고 넘김
                else:
                    step_d = (step_d + 2) % 4
            '''
            # 만약 증가하는 방향으로 간다면, 더해주면 됨
            # 만약 감소하는 방향으로 간다면, 빼주면 됨
            cr, cc = now_r, now_c
            nr, nc = now_r, now_c
            if d == 0:  # 증가 방향, 행 이동
                cr -= 1



            # 종료 후 토끼 이동 위치 우선순위 반영하기 위해서
            heapq.heappush(turn_heap, (-(nr + nc), -nr, -nc, d))
        X, nxt_r, nxt_c, nxt_dir = heapq.heappop(turn_heap)
        # 최대heap 사용으로 인한 - 변환
        nxt_r, nxt_c, nxt_dir = (-nxt_r, -nxt_c, -nxt_dir)

        # 점수 반영
        total_sum += (nxt_r + nxt_c)
        rabbits_score[pid_i] -= (nxt_r + nxt_c)


        # 토끼를 이동 - 전체 info
        rabbits_info[pid_i] = (d_i, nxt_r, nxt_c)

        # 토끼의 점프 결과를 반영해서, 추가로 넣어줌
        heapq.heappush(jump_heap, (now_j+1, nxt_r+nxt_c, nxt_r, nxt_c, pid_i, d_i))
        # 점프 토끼 정보 갱신
        current_rabbit_info = (nxt_r+nxt_c, nxt_r, nxt_c, pid_i)
        if current_rabbit_info > best_rabbit_of_round:
            best_rabbit_of_round = current_rabbit_info

        # 점수가 누적되어야 한다!

        # test print
        # for key in rabbits_info.keys():
        #     print(f"{key}: {rabbits_info[key]}")
        #     print(f"score:::{key}: {rabbits_score[key]}")

    # 추가 점수를 주기 위함
    if best_rabbit_of_round[3] != -1:
        rabbits_score[best_rabbit_of_round[3]] += S

    # test print
    # print('add')
    # for key in rabbits_info.keys():
    #     print(f"{key}: {rabbits_info[key]}")
    #     print(f"score:::{key}: {rabbits_score[key]}")

def change_dist(command):
    pid, L = map(int, command[1:3])
    d, r, c = rabbits_info[pid]
    rabbits_info[pid] = (L*d, r, c)

def best_member(command):
    global total_sum
    best_score = 0
    for rabbit in rabbits_score:
        if rabbits_score[rabbit] > best_score:
            best_score = rabbits_score[rabbit]
    return total_sum + best_score

Q = int(input())

# Q개의 명령을 입력받음
for _ in range(Q):
    command_line = input().split()

    if command_line[0] == '100':
        # 100 N M P pid_1 d_1 pid_2 d_2 ... pid_p d_p
        # 경주 시작 준비
        init(command_line)

        # test print
        # for key in rabbits_info.keys():
        #     print(f"{key}: {rabbits_info[key]}")

    elif command_line[0] == '200':
        # 200 K S - 최대 2000번
        # 경주 진행
        start_race(command_line)

    elif command_line[0] == '300':
        # 300 pid_t L - 최대 2000번
        change_dist(command_line)
    else:
        # 400 - 정확히 마지막 명령으로만 주어짐
        # 항상 주어짐
        best_score = best_member(command_line)
        print(best_score)