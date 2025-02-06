# 설명
# 각 자리가 숫자(0~9)로만 이루어진 문자열 S
# 모든 숫자 사이에 x or + 넣어 만들 수 있는 가장 큰 수
# 모든 연산은 왼쪽에서부터 진행됨
import sys
input = sys.stdin.readline

s = input()
res = 1

for i in range(0, len(s) - 1):
    d = int(s[i])
    if res == 0:
        res += d
    else:
        res *= d
print(res)