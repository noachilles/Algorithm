# 설명
# 일직선 상에서 인접하지 않은 블럭을 취해 최댓값을 구하기

# 입력
# N: 식량창고 개수
# K: 각 식량창고에 저장된 식량 개수

n = int(input())
k = list(map(int, input().split()))

d = [0] * 101
d[0] = k[0]

# 교재에 소개된 예제는 맞았지만, 몇가지 상황을 고려하지 못함
d[1] = k[1]
for i in range(3, n):
    d[i] = k[i]
    d[i] += max(d[i-2], d[i-3])

# 아래 내용은 교재 해설 참고한 코드, 점화식을 정확히 세우자
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])
    
print(d[n-1])
