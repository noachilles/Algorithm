# 설명
# 알파벳 대문자와 0~9로만 구성된 문자열
# 모든 알파벳 오름차순 정렬해 출력 후, 모든 숫자를 더한 값을 이어서 출력

s = input()
num = []
al = []

for i in s:
    if i >= '0' and i <= '9':
        num.append(int(i))
    else:
        al.append(i)
al.sort()

for i in al:
    print(i, end='')
print(sum(num))
