# binary search 실전 1
# 설명
# 매장 부품 N개, 정수 형태 고유 번호
# M개 종류 부품 대량 구매 -> 모두 있는지 확인하는 프로그램

# 입력
# 1: n
# 2: n개 정수(공백 구분)
# 3: m
# 4: m개 정수(공백 구분)

import sys

def binary_search(array, target, start, end):
    # 결과를 하나씩 출력할 수도 있고, result에 담아서 출력할 수도 있음
    # array와 target을 하나씩 받는다면 하나씩 출력하는 게 맞고, 
    # result에 담으려면 함수 내부에서 반복하는 것이 좋음
    # 그럼 인자 수가 더 많아지므로, 하나씩 출력하자(외부 반복문)
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
nread = sys.stdin.readline().rstrip()
nlist = nread.split()
nlist.sort()
m = int(input())
mread = sys.stdin.readline().rstrip()
mlist = mread.split()

for target in mlist:
    temp = binary_search(nlist, target, 0, n-1)
    if temp == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')