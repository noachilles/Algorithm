# quick sort
# O(NlogN) / worst: O(N^2) - for sorted data

n = int(input())
lst = list(map(int, input().split()))


def quick_sort(lst, start, end):
    if start >= end:
        return
    p = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and lst[left] <= lst[p]:
            left += 1
        while right > start and lst[right] >= lst[p]:
            right -= 1
        if left > right:
            lst[p], lst[right] = lst[right], lst[p]
        else:
            lst[left], lst[right] = lst[right], lst[left]
    quick_sort(lst, start, right) # 값을 변경한다고 해서 index가 바뀌지는 않음
    quick_sort(lst, right+1, end) 
    
def quick_sort_2(lst):
    if len(lst) <= 1:
        return lst
    
    p = lst[0]
    tail = lst[1:]
    
    left_side = [x for x in tail if x <= p]
    right_side = [x for x in tail if x > p]
    
    return quick_sort_2(left_side) + [p] + quick_sort_2(right_side)
    

quick_sort(lst, 0, n-1)
lst2 = quick_sort_2(lst)
print(*lst)
print(*lst2)