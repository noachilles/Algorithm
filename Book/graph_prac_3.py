# 설명
# 선수 강의가 있는 강의는 선수 강의 먼저 들어야 함
# 총 N개의 강의를 듣고자, 모든 강의는 1번 ~ N번 번호 가짐
# 동시에 여러 개 강의 들을 수 있음
# 1, 2번 강의는 선수 강의 없고, 1, 2를 들어야 강의 3을 들을 수 있다고 하자.
# 1: 30시간, 2: 20시간, 3: 40시간이 소요된다면
# 1, 2를 동시에 들을 수 있으므로 30시간 + 강의 3을 수강할 때 40시간 총 70시간이 소요된다.
# N개의 강의에 대해 수강하기까지 걸리는 최소 시간 각각 출력

# 입력
# N: 강의 수(<= 500)
# 강의 시간, 먼저 들어야 하는 강의들의 번호
# 각 줄은 -1로 끝남

# 출력
# N개의 강의에 대해 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력

import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().rstrip().split()))
    time[i] = data[0]
    for x in data[1: -1]:
        indegree[i] += 1
        graph[x].append(i)
    
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        # now를 수강해야 수강할 수 있는 강의 i에 대해
        for i in graph[now]:
            # result[i]와 result[now] + time[i] 중 더 큰 값이 result[i]
            # 인접한 노드에 대해 현재보다 강의 시간이 더 긴 경우를 찾으면, 더 오랜 시간이 걸리는 경우의 시간 값을 저장 -> 결과 테이블을 갱신
            # 어차피 indegree가 0이면 처음부터 queue에 들어가므로, 그들은 아래의 연산에 서로 해당하지 않음
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])

topology_sort()