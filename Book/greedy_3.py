# 숫자 카드 게임 - 이코테
# 입력
# (숫자 카드들이 놓인 행의 개수, N) (열의 개수, M)
# N개의 줄에 걸쳐 각 카드에 적힌 숫자 주어짐
# 출력
# 게임 룰에 맞는 결과

n, m = map(int, input().split())
matrix = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))
    matrix[i].sort()

big_first = matrix[0][0]
for i in range(n):
    if matrix[i][0] > big_first:
        big_first = matrix[i][0]
        
print(big_first)
