# quick sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort1(array, start, end):
    if start >= end: # 원소가 1개인 경우
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right: # 서로 엇갈리지 않은 경우
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피ㅣ벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
        
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)
    
def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오늘쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)
    

# quick_sort1(array, 0, len(array)-1)
# print(array)

# 새로운 리스트를 반환하기 때문에 array 자체는 업데이트X
print(quick_sort2(array))