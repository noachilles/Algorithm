import sys

def binary_search(array, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1            
    return 0

n = int(input())
array = sys.stdin.readline().rstrip()
array = list(map(int, array.split()))
array.sort()
m = int(input())
target = sys.stdin.readline().rstrip()
target = list(map(int, target.split()))
res = []

for t in target:
    res.append(binary_search(array, t, 0, n-1))

for _ in res:
    print(_, end=' ')