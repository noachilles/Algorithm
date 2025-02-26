def dfs(o1, res):
    v[o1] = 1
    d[o1] = res
    res += 1
    # print(o1)
    for key in arr[o1]: # key에 대해
        if not v[key]: # 방문 기록이 없다면
            dfs(key, res)
            v[key] = 1
  
d = dict()      
n = int(input())
arr = [[] for _ in range(n+1)]
v = [0] * (n+1)
o1, o2 = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
dfs(o1, 0)
if o2 in d:
    print(d[o2])
else:
    print(-1)