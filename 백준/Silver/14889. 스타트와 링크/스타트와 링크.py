'''
N명의 사람, N은 짝수
N/2명으로 이루어진 스타트팀 / 링크팀

능력치 S_ij는 i번, j번이 같은 팀에 속했을 때, 팀에 더해지는 능력치  
팀의 능력치: 팀에 속한 모든 쌍의 능력치 S_ij의 합
S_ij != S_ji
team(i, j) = S_ij + S_ji

팀의 능력치 차이를 최소로
(1, 4), (2, 3) => 6, 6

S)  
문제를 풀이하려면, 모든 조합의 쌍을 구해야 함
단, (1, 4)를 선택한 경우와 (2, 3)을 선택한 경우는(예시에서) 같으므로
굳이 두 번을 해줄 필요 X
이 점을 생각해서 들어가자
N <= 20이므로 크지 X

'''

# 경험치를 저장할 리스트
ex_list = []
# combinations는 조합을 구하고, 경험치 연산까지 수행
def combinations(start, n, arr):
    if len(arr) == n:
        # 경험치 연산
        ex = 0
        for i in range(n):
            for j in range(i+1, n):
                a, b = arr[i], arr[j]
                ex += (each_score[a][b] + each_score[b][a])
        ex_list.append(ex)
    for i in range(start, N):
        combinations(i+1, n, arr+[i])

# input
N = int(input())

each_score = []
for _ in range(N):
    each_score.append(list(map(int, input().split())))

# 반환할 결과: output
res = float('inf')
# 모든 조합에 대한 경험치를 구함
combinations(0, N//2, [])

# ex_list에 대해, 좌우 각 끝이 서로소
# 두 조합의 경헙치 차를 구해서 비교함
l = len(ex_list)
for i in range(l):
    j = l - 1 - i
    if j <= i:
        break
    res = min(res, abs(ex_list[i] - ex_list[j]))
print(res)