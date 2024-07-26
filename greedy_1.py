# 큰 수의 법칙 - 이코테

# 입력
# (배열 크기,N) (숫자가 더해지는 횟수,M) (같은 수 반복해 더할 수 있는 횟수 제한,K)
# 배열

# 출력
# 더해진 답  

# Greedy

# n, m, k 공백 구분 입력 받기
n, m, k = map(int, input().split())
# n개 값을 가진 data 입력 받기
data = list(map(int, input().split()))

# 정렬 (asc)
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0: # k가 m보다 크다면 가장 큰 수로 끝낼 수 있으므로
        break
    result += second
    m -= 1
    
print(result)

'''
In
5 8 3
2 4 5 4 6
Out
46
'''