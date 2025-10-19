'''
1. 배열에 자연수 x 넣음
2. 배열에서 가장 작은 값 출력, 제거 - pq의 pop
'''

# priority queue 만들기
import heapq
import sys

input = sys.stdin.readline

pq = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(pq, x)
    # x가 0이면 배열에서 가장 작은 값 출력, 값을 배열에서 제거
    else:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)
