# 설명
# N을 자릴수 기준으로 반을 나누고
# 왼쪽 부분의 각 자릿수 합광 오른쪽 각 자릿수 합을 더한 값이 동일한지 판단

# 입력
# 자릿수가 짝수인 N이 정수로 입력

# 출력
# 위 조건 만족하면 "LUCKY", 만족하지 않으면 "READY" 출력

def add_all(s):
    num = 0
    for i in s:
        num += int(i)
    return num

n = input()
mid = (len(n) - 1) // 2 + 1

left = n[:mid]
right = n[mid:]

if add_all(left) == add_all(right):
    print("LUCKY")
else:
    print("READY")