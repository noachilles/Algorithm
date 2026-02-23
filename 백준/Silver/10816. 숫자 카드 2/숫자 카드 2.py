import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input())
b = list(map(int, input().rstrip().split()))

cnt_dict = Counter(a)
for target in b:
    print(cnt_dict[target], end=' ')
    