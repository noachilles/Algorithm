# 설명
# 각 자리가 숫자(0~9)로만 이루어진 문자열 S
# 모든 숫자 사이에 x or + 넣어 만들 수 있는 가장 큰 수
# 모든 연산은 왼쪽에서부터 진행됨
import sys
input = sys.stdin.readline

s = input()
res = int(s[0])

for i in range(1, len(s) - 1):
    num = int(s[i])
    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num

print(res)