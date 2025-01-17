# insert sort
# O(N^2) / best: O(N) - with almost sorted data
import time


n = int(input())
lst = list(map(int, input().split()))

s = time.time()

for i in range(1, n):
    for k in range(i, 0, -1):
        if lst[k] < lst[k-1]:
            lst[k], lst[k-1] = lst[k-1], lst[k]
        else:
            break
end = time.time()

print(lst, '\n', end-s)