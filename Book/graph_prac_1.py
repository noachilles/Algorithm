# 설명
# 0번 ~ N번: 모든 학생이 서로 다른 팀으로 구분, N + 1개 팀이 존재
# 1. 팀 합치기: 두 팀을 합침
# 2. 같은 팀 여부 확인: 두 학생이 같은 팀인지 확인

# 입력
# N, M: 팀의 번호, 입력으로 주어지는 연산 개수
# M개 줄: 각각의 연산
# 팀 합치기: 0 a b
# 확인 연산: 1 a b -> YES or NO 로 결과 출력

import sys
input = sys.stdin.readline

def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

def check_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a == b:
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())
team = [0] * (n + 1)

for i in range(1, n + 1):
    team[i] = i

for _ in range(m):
    f, a, b = map(int, input().split())
    if f == 0:
        union_team(team, a, b)
    elif f == 1:
        check_team(team, a, b)
    else:
        print("UNDEFINED FUNCTION")