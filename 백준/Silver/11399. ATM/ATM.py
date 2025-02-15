import sys
input = sys.stdin.readline

n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
for i in range(n-1):
    p_list[i+1] = p_list[i] + p_list[i+1]
print(sum(p_list))