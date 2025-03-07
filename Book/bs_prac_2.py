# binary search 실전 2
# 설명
# 절단기에 높이 h를 지정 -> 줄지어진 떡을 한 번에 절단
# 높이 > h 이면 윗부분 잘림 / 높이 <= h 이면 잘리지 X
# 손님이 가져가는 떡의 길이는 잘린 길이
# ex) 19cm 떡이 있고, 15cm만큼 자른다면 4cm를 가져감

# 입력
# n(떡 개수), m(원하는 길이)
# 떡의 길이

# 출력
# m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
# 가능하면 1 늘림 -> 
# 안 되면 1 줄임

# index를 사용하면 값을 모두 돌아볼 수 없음, 0에서부터 시작해 가장 큰 값의 '값'으로 접근해야 함
def binary_search(array, m, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    res = 0 
    for v in array:
        if v > mid:
            res += (v - mid)
    if res == m:
        return mid
    elif res > m:
        return binary_search(array, m, mid+1, end)
    else:
        return binary_search(array, m, start, mid-1)
    
h = binary_search(array, m, 0, array[-1])
print(h)
