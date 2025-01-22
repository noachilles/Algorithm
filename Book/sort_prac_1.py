# sort 실전 문제 1

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분해 출력

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')