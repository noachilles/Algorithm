# 설명
# 주어진 수를 M번 더해 가장 큰 수를 만드는 법칙
# 특정 인덱스 수가 연속 K번을 초과해 더해질 수 없음

# 입력
# N, M, K

# k개 만큼 더할 수 있음 -> k * array[0]
# 그 다음은 array[1]을 더하고
# 다시 k * array[0] 

# k만큼 몇 번 더할 수 있을지 고민하자
# k가 3이고 m이 7일 때, 3 + 1 + 3
# m이 6일 때 3 + 1 + 2
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)
res = 0

cnt = (m // (k + 1)) 
res = cnt * k * array[0] + cnt * array[1]
cnt = m - cnt * (k + 1)
res += cnt * array[0]
print(res)