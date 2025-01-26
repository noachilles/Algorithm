n = int(input())
array = [0] * 10

k = 10
while n > 0:
    v = n % k
    n //= k
    array[v] += 1

for i in range(len(array)-1, -1, -1):
    while array[i] > 0:
        print(i, end='')
        array[i] -= 1
    