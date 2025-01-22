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

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)