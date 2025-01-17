# count sort
# O(N + K) 
# some constraints:
# 1. less than 1,000,000 of data
# 2. only for integer data

n = int(input())
lst = list(map(int, input().split()))
cnt_lst = [0 for _ in range(max(lst) + 1)]

for i in lst:
    cnt_lst[i] += 1
    
for i in range(len(cnt_lst)):
    for j in range(cnt_lst[i]):
        print(i, end=' ')