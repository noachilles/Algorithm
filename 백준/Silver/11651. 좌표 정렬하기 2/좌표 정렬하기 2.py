n = int(input())
array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array = sorted(array, key=lambda x : (x[1], x[0]))
for t in array:
    print(t[0], t[1], end="\n")