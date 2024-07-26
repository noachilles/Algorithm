# 이코테 예제 4-2

# 입력
# (N시 59분 59초의 N)
# 출력
# 00시 00분 00초부터 N시 59분 59초까지 3이 하나라도 포함되는 경우의 수

n = int(input())
res = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in (str(i) + str(j) + str(k)):
                res += 1
print(res)