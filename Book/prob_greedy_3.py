# 설명
# 0과 1로만 이루어진 문자열 S
# 숫자를 전부 같게 만들려고 함 -> 연속된 하나 이상의 숫자를 모두 뒤집는 것: 1을 0으로, 0을 1로
# S = 0001100 일 때,
# 4, 5번째 문자를 뒤집으면 0000000 -> 행동 최소 횟수가 1
import sys
input = sys.stdin.readline

s = input()
cnt = 0
for i in range(1, len(s) - 1):
    if s[i] != s[i-1]:
        cnt += 1
print(cnt // 2 + cnt % 2)