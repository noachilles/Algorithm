# 이코테 실전문제 6-3

# 입력
# (배열들의 원소 개수 N, 바꿔치기 가능 횟수 K)
# (배열 A, 공백 구분)
# (배열 B, 공백 구분)

# 출력
# 배열 A 원소 합 최댓값

# 선택정렬처럼 진행하면 될듯  

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
while k > 0:
    min_i = 0
    max_i = 0
    for i in range(1, n):
        if a[i] < a[min_i]:
            min_i = i
    for i in range(1, n):
        if b[i] > b[max_i]:
            max_i = i
    a[min_i], b[max_i] = b[max_i], a[min_i]
    k -= 1

print(sum(a))