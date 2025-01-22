# boj 11399
# (입력)
# (사람 수, N)
# (인출 시간, P_i)
# (출력)
# 각 사람이 돈을 인출하는 데 필요한 시간(대기+인출) 합의 최솟값

n = int(input())
pi = list(map(int, input().split()))
pi.sort()
# sum을 초기화할 때 바로 pi를 대입하면 얕은복사가 일어남
sum = [i for i in pi]
res = 0
for i in range(1, n):
    for j in range(0, i):
        sum[i] += pi[j]
    res += sum[i]
res += sum[0]
print(res)