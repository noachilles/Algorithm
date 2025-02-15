import sys
input = sys.stdin.readline

def binary_search(start, end, target, array):
    while(start <= end):
        mid = (start + end) // 2
        if target == array[mid][0]:
            return array[mid][1]
        elif target < array[mid][0]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input())
b = list(map(int, input().rstrip().split()))

a.sort()
s = set(a)
res = [0] * m # 결과

array = []
cnt = 1
for i in range(0, n-1): # O(N)
    if a[i] != a[i+1]: # 다음 값과 다르다면
        k = a[i]
        array.append((a[i], cnt))
        cnt = 1
    else: # 다음 값과 같다면
        cnt += 1
array.append((a[-1], cnt))

for i in range(m):
    res[i] = binary_search(0, len(array) - 1, b[i], array)

for item in res:
    print(item, end=' ')