n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((int(input_data[0]), input_data[1], i))

array.sort(key=lambda member: (member[0], member[2]))
for member in array:
    print(member[0], member[1])