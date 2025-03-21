def combinations(m, new, start):
    global survive
    if len(new) == m:
        # new에 있는 것들로 치킨집을 고른다
        f(new)
        return 
    for i in range(start, chicken):
        combinations(m, new + [i], i + 1)

def f(survive):
    global mn, dist
    cdist = 0
    for j in range(house):
        # 각 집에서 가장 가까운 치킨 거리를 저장할 변수
        closest = 25001
        for ch in survive:
            closest = min(closest, dist[j][ch])
        cdist += closest
    mn = min(cdist, mn)

if __name__ == "__main__":

    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 전체 중 치킨집의 개수와 거리를 저장, 집의 개수와 거리를 저장
    house = 0
    house_xy = []
    chicken = 0
    chicken_xy = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                house += 1
                house_xy.append((j, i))
            elif grid[i][j] == 2:
                chicken += 1
                chicken_xy.append((j, i))

    # 각 집에서 치킨집까지 거리를 계산해 저장
    dist = [[0] * chicken for _ in range(house)]
    for i in range(house):
        for j in range(chicken):
            h_x, h_y = house_xy[i]
            c_x, c_y = chicken_xy[j]
            dist[i][j] = abs(h_x - c_x) + abs(h_y - c_y)

    mn = 10 ** 6
    combinations(M, [], 0)
    print(mn)