robot = []
N, K = map(int, input().split())
belt = list(map(int, input().split()))
cnt = 0
t = 0
while True:
    t += 1
    temp = []
    # 1번째 단계
    belt = belt[2*N-1:] + belt[:2*N-1]
    for i in range(len(robot)):
        if robot[i] + 1 < N-1:
            temp.append(robot[i] + 1)
    robot = temp[:]

    # 2번째 단계
    robot.sort()
    for i in range(len(robot)-1, -1, -1):
        # 만약 앞으로 이동할 수 있다면 - (로봇X)
        if belt[robot[i]+1] > 0 and (robot[i]+1) not in set(robot):
            if (robot[i] + 1) < N:
                robot[i] += 1
                belt[robot[i]] -= 1
                if belt[robot[i]] == 0:
                    cnt += 1
                if robot[i] == N:
                    robot.pop()
    # 개수 확인...
    if cnt >= K:
        print(t)  
        break

    # 3번째 단계
    # 올리는 자리의 내구도가 0보다 크면
    if belt[0] > 0:
        belt[0] -= 1
        robot.append(0)
        if belt[0] == 0:
            cnt += 1
    
    # 개수 확인...
    if cnt >= K:
        print(t)  
        break