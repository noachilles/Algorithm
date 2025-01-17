# insert sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]: # 오른쪽에 있는 데이터의 값이 더 크다면
            array[j], array[j - 1] = array[j - 1], array[j] # swap
        else:
            break
print(array)