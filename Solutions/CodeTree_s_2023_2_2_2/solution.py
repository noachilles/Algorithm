"""
# CodeTree 코드트리 오마카세

각 초밥에 사람 이름을 적어서 회전하는 베르 위에 올려놓는 초밥 오마카세

- 원형 형태의 초밥 벨트와 L개의 의자
- 의자는 원형에서 x=0을 기점으로 시계방향으로 돌아 x=1~L-1까지 총 L개가 등간격

[회전초밥]
- 각 의자 앞에 여러 개 놓일 수 있음
- 초밥 벨트는 1초에 한 칸씩 시계방향으로 회전함

[초기셋팅]
- 벨트 위에 놓인 초밥이 전혀 없음
- 의자 위에 앉아 있는 사람도 없음

--- 기능 소개

[1. 주방장의 초밥 만들기]
- 주방장은 시각 t에 위치 x 앞에 있는 벨트 위에 name 이름을 부착한 회전 초밥 하나를 올려둠
    시각 t: x 앞에 있는 벨트 위에 name 이름 부착한 회전 초밥 하나 올림
- 시각 t에 초밥 회전이 일어난 직후에 발생
- 같은 위치에 여러 회전 초밥이 올라갈 수 있음
- 자신의 이름이 적혀 있는 초밥이 같은 위치에 여러 개 놓이는 것도 가능

[2. 손님 입장]
- 시각 t: 이름 - name, 위치 - x
- 시각 t에 초밥 회전이 일어난 직후에 발생함
- x 앞으로 오는 초밥들 중 자신의 이름이 적혀있는 초밥을 정확히 n개 먹음(n개보다 적다면?)
- 이 명령이 주어졌을 때, 해당 위치에는 사람이 없음을 가정해도 괜찮음
- 시각 t에 위치 x에 자신의 이름이 적혀있는 초밥이 놓여 있다면 자리에 착석하는 즉시 먹게 됨
- 자신의 이름이 적혀 있는 초밥이 같은 위치에 여러 개 - 여러 개 먹을 수도 있음
- 초밥을 먹는 데에는 시간이 소요되지 않음

[3. 사진 촬영]
- 시각 t에 코드트리 오마카세 집의 모습을 촬영
- 시각 t)
    1. 초밥 회전
    2. 손님이 자신이 앉아 있는 자리에서 자신의 이름이 적힌 초밥을 먹음
    3, 그 다음, 사진 촬영
    4. 사진 촬영을 진행했을 때 현재 초밥집에 있는 (사람 수, 남아 있는 초밥 수)

**[핵심 논리 수정]
1. 초밥의 소멸 시간 계산
    - 초밥이 벨트에 올라오는 순간, 이미 손님이 있거나 나중에 올 손님의 위치를 고려
    - 정확히 몇 초에 이 초밥이 사라질지 수학적으로 계산
2. 손님의 퇴장 시간 계산
    - 손님이 먹어야 할 n개의 초밥 중 가장 마지막에 먹히는 초밥의 소멸 시간 = 손님이 나가는 시간
3. 이벤트 통합
    - 초밥 추가 (시각 t, +1 초밥)
    - 손님 입장 (시각 t, +1 사람)
    - 초밥 소멸 (시각 t_death, -1 초밥)
    - 손님 퇴장 (시각 t_exit, -1 사람)
    - 사진 촬영 (시각 t, 결과 출력)
    => 모든 이벤트를 하나의 리스트에 넣고, 시간순으로 정렬한 뒤 딱 한 번만 훑기!
"""

# 1. 1초에는 하나의 초밥만 만들 수 있음 -> ID로 사용함
# 2. s(ushi)_info: 초밥을 저장해 두는 dictionary {ID: (t, name)}
# 3. c(ustomers)_info: 사람 별 조회가 가능하도록 저장해 두는 dictionary {name: [[t1, t2, t3,...], x, n, in_store(T/F)]}
# 4. 판매되었는지, 아직 남아있는지 조회하기 위한 set sold=set()

import heapq

# ** 수정 로직
sushi_list = dict()
customer_dict = dict()
customer_ate = dict()

events = [] # (시간, 우선순위, 초밥변화량, 사람변화량)
''' 우선순위
1. 초밥 생성
2. 손님 입장
3. 초밥 소멸
4. 손님 퇴장
'''

# 초밥, 사람 수
numbers_of_sushi = 0
numbers_of_customers = 0
index = 0

def make_sushi(t, x, name):
    # s_info, c_info에 각각 정보를 저장함
    # init과 같은 역할을 수행함
    # ** 수정 이후 로직
    # 1. 이름별 초밥 목록에 초밥을 추가함
        # 만약 dictionary에 초밥 리스트가 생성되지 않은 경우 추가해줌
    heapq.heappush(events, (t, 1, 1, 0))

    # 손님이 이미 가게에 있다면
    if name in customer_dict:
        tc, xc, nc = customer_dict[name]
        if customer_ate[name] == nc:
            return
        dist = (xc - x + L) % L
        heapq.heappush(events, (t + dist, 2, -1, 0))
        customer_ate[name] += 1
        if customer_ate[name] == nc:
            heapq.heappush(events, (t + dist, 2, 0, -1))
    else:
        if name not in sushi_list:
            sushi_list[name] = []
        sushi_list[name].append((t, x))

def enter_customer(t, x, name, n):
    # c_info[name]에 정보를 저장함(t도 필요할까?)
    # c_info에 기존에 포함된 초밥 ID 조회
        # 1. 현재 위치가 x인 초밥이 있는지 연산으로 확인((t_n - t + x) % L))
        # 2. 아직 남아있는지 확인(sold에 포함되지 X)
        # 3. 만약 초밥이 있다면, 먹고 c_info의 정보 및 s_info의 정보 갱신
    # ** 수정 이후 로직
    # 1. 이름을 key로, 입장 정보를 저장함
    customer_dict[name] = (t, x, n)
    # 2. 손님 입장 이벤트를 생성함
    # 3. 손님은 아직 초밥을 섭취하지 않음 -> ate dict 초기화
    customer_ate[name] = 0

    heapq.heappush(events, (t, 1, 0, 1))
    if name in sushi_list:
        for ts, xs in sushi_list[name]:
            poss = (xs + (t - ts)) % L
            dist = (x - poss + L) % L
            heapq.heappush(events, (t + dist, 2, -1, 0))
            customer_ate[name] += 1
            if customer_ate[name] == n:
                heapq.heappush(events, (t + dist, 2, 0, -1))

    # 먹은 초밥들을 초기화
    sushi_list[name] = []

def capture_picture(t):
    # t 시간에 사람 수, 초밥 수 두 개를 구하면 됨
    # 여기에서 모든 작업을 수행함.
    # 여태까지 enter한 손님들의 각 기록을 조회하면서, 먹을 수 있는 초밥의 위치를 판단함
    # 초밥들의 위치를 바탕으로, 함수 실행 시점에 이미 먹혔을지, 먹히지 않았을지 판단
    # ** 초밥이 제자리로 돌아오는 사이에, name이 동일한 customer가 있다면 반드시 먹히게 되어있음
    # 손님이 위치한 x를 기준으로 먼저 먹히는 초밥을 따로 연산해야 할 것 같음
    # 또한 하나의 위치에 여러 개의 동일한 이름을 가진 초밥이 올라갈 수 있으므로, 이 점을 참고!
    # 개수를 저장하는 변수를 전역으로 설정하자

    # ** 수정 이후 로직
    # 1. 여태까지 쌓인 것들을 살펴보면서 초밥 생성, 손님 입장 이벤트를 events에 추가
    # 초밥이 소멸하거나, 손님이 나가는 경우는 모두! 손님이 초밥을 먹어서 생기는 이벤트
    # 즉, 손님이 필요하고, 손님의 이름으로 만들어진 초밥이 필요하다
    global numbers_of_sushi, numbers_of_customers

    # 만약 초밥이 이미 있다면, 초밥의 손님 입장 시점을 고려해서 소멸 계산
    # 손님이 먼저 와있거나, 동시에 왔다면
    # 초밥이 이동해야 할 거리를 계산해서 소멸 계산
    # 2. 이후 초밥 소멸, 손님 퇴장 이벤트를 events에 추가
    # 3. sort
    # 4. sort 이후 하나씩 훑으면서 변화량을 적용함
    # 5. 출력

    # test print
    # for item in events:
    #     print(item)

    # 힙이 비어있지 않고, 가장 빠른 이벤트 시간이 사진 찍는 시점보다 작거나 같을 때
    while events and events[0][0] <= t:
        te, prio, delta_sushi, delta_customers = heapq.heappop(events)

        numbers_of_sushi += delta_sushi
        numbers_of_customers += delta_customers
    return

# import sys
# sys.stdin = open('input.txt', 'r')

# 초밥 벨트의 길이 L, 명령의 수 Q
L, Q = map(int, input().split())
for q in range(Q):
    cmd = input().split()
    if cmd[0] == '100':
        # 초밥 만들기
        # 100 t x name
        t, x= map(int, cmd[1:3])
        name = cmd[3]
        make_sushi(t, x, name)

    elif cmd[0] == '200':
        # 손님 입장
        # 200 t x name n
        t, x = map(int, cmd[1:3])
        name = cmd[3]
        n = int(cmd[4])
        enter_customer(t, x, name, n)
    else:
        # 사진 촬영
        # 300 t
        t = int(cmd[1])
        capture_picture(t)
        print(f"{numbers_of_customers} {numbers_of_sushi}")