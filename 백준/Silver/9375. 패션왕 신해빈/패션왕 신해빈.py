'''
T는 최대 100
의상 최대 30
의상 이름 / 의상 종류 공백 구분
만약 모든 의상이 종류가 다르다고 하면  
Combinations(30, 1~30)
한 개 고르는 경우, 두 개 고르는 경우... n개 고르는 경우
핵심: combination을 하나씩 구하면 O(2^N*N)으로 시간초과
모자 3개 - 모자1, 모자2, 모자3, 모자 쓰지 X
상의 2개 - 상의1, 상의2, 상의 X
'''

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 해빈이의 옷장
    closet = dict()
    for _ in range(n):
        name, type = input().split()
        if type in closet:
            closet[type] += 1
        # 입는다, 입지 않는다 2개의 경우의 수
        else:
            closet[type] = 2

    types = len(closet)

    res = 1
    for k in closet.values():
        res *= k
    # 아무것도 입지 않는 경우의 수 1을 빼줌
    print(res - 1)