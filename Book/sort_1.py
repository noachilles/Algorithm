# select sort
# O(N^2)

import time

n = int(input())
lst = list(map(int, input().split()))

s = time.time()

for i in range(n):
    min_i = i
    for j in range(i+1, n):
        if lst[j] < lst[min_i]:
            min_i = j
    lst[i], lst[min_i] = lst[min_i], lst[i]

end = time.time()
            
print(lst, '\n', end-s)