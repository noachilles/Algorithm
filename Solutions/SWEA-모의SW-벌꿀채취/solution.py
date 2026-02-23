# 26-01-26
'''
모든 벌꿀을 살피면서, 값이 최대가 되는 경우를 찾자 -> 일단 전체 탐색
1. 각 통별로 합이 C를 초과하지 않는지 확인해야 함
2. 개별 꿀의 제곱을 구해야 함
'''

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    
    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    print(grid)

    '''
    만약 현재 c가 N-M+1 이상이라면, 다음줄로 넘어간다
    그럼 그 줄에서의 칸들을 살핌
    칸에 대해서, 만약 합이 C 이상이라면 그 중에서 가장 큰 합을 골라야겠지
    -> M개부터 1개까지 살펴보면서 combinations
    '''
    for r in range(N):
        for c in range(N-M+1):
            # 여기서 value 값을 구해야 함
            # 두 개를 어떻게 따로 선택할까?