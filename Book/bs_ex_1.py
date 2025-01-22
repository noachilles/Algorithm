# binary search example code 1

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        # end를 mid 앞으로 옮김 - return 필수!
        return binary_search(array, target, start, mid-1)
    else:
        # stt를 mid 뒤로 옮김
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print('{}은 array의 {}번째 원소입니다.'.format(target, result + 1))