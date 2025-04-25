T = int(input())
res = [0] * 3
flag = False

while not flag:
    if T >= 300:
        res[0] += T // 300
        T %= 300
    elif T >= 60:
        res[1] += T // 60
        T %= 60
    else:
        res[2] += T // 10
        T %= 10
        flag = True
        
if T > 0:
    print(-1)
else:
    for i in range(3):
        print(res[i], end=' ')