# 드래곤 커브 그리기
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# 오른쪽, 위쪽, 왼쪽, 아래쪽

grid_lst = []
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

def f(x, y, new):
    global stack
    for i in range(len(stack) - 1, -1, -1):
        d = (stack[i] + 1) % 4
        # 방향 갱신 이후 드래곤 커브를 그린다
        x, y = draw(x, y, d)
        new.append(d)
    return x, y

def draw(x, y, d):
    nx, ny = x + directions[d][0], y + directions[d][1]
    if 0 <= nx <= 100 and 0 <= ny <= 100:
        grid_lst.append((nx, ny))
    return (nx, ny)
    

# array의 값들은 한 번만 사용되면 된다
for i in range(N):
    stack = []
    x, y, d, g = array[i]
    stack.append(d)
    if 0 <= x <= 100 and 0 <= y <= 100:
        grid_lst.append((x, y))
    x, y = draw(x, y, d)
    for j in range(g):
        new = []
        x, y = f(x, y, new)
        stack.extend(new)
ans = 0
s = set(grid_lst)
for dot in s:
    x, y = dot
    if (x+1, y) in s and (x+1, y+1) in s and (x, y+1) in s:
        ans += 1
print(ans)