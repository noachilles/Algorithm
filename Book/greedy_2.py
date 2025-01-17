# greedy_1 문제의 M 범위가 커질 때, 시간 초과를 해결
# if M = 8, K = 3, data = [2, 4, 5, 4, 6]일 때
# (6 + 6 + 6 + 5) + (6 + 6 + 6 + 5)
# 가장 큰 수가 더해지는 개수는 int(M / (K+1)) * K + M % (K+1)
# M / (K+1)은 수열의 등장 횟수를 구하기 위함, 여기에 K를 곱해야 결과가 최댓값일 때 '가장 큰 수의 개수'

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
result += first * (int(m/(k+1)) * k + m % (k+1))
result += second * (int(m/(k+1)))

print(result)


'''
In
5 8 3
2 4 5 4 6
Out
46
'''