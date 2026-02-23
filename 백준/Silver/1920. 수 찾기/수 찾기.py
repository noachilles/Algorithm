import sys
input = sys.stdin.readline

def binary_search(start, end, target, array):
    while(start <= end):
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input())
b = list(map(int, input().rstrip().split()))

a.sort()

for target in b:
    res = binary_search(0, n-1, target, a)
    if res == -1:
        print(0)
    else:
        print(1)