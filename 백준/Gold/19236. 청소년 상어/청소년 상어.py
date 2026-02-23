def move_fish(shark, fish, grid):
    # 물고기를 이동시킨다
    # 반환할 이차원 배열
    result = [arr[:] for arr in grid]
    for i in sorted(fish): 
        x, y = fish[i] 
        move = False
        d = result[y][x][1] - 1
        d1 = d
        while not move:
            nx, ny = x + directions[d][0], y + directions[d][1]
            # 범위 내에서
            if 0 <= nx < 4 and 0 <= ny < 4:
                # 상어가 없다면
                if (nx, ny) != shark:
                    # 다른 물고기가 있는 자리라면 - 자리 바꿈
                    if result[ny][nx][0] in fish:
                        fish[i] = (nx, ny)
                        fish[result[ny][nx][0]] = (x, y)
                        result[ny][nx], result[y][x] = (result[y][x][0], d+1), result[ny][nx]
                    # 다른 물고기가 없는 자리라면 - 그냥 이동
                    else:
                        result[ny][nx], result[y][x] = (result[y][x][0], d+1), (0, 0)
                        fish[i] = (nx, ny)
                    # 살아있는 물고기 위치도 이동
                    move = True
                    break
            # 상어가 있거나 범위를 벗어난다면
            # 방향을 바꾼다
            d = (d + 1) % 8
            # 다시 원방향으로 돌아오면 break
            if d == d1:
                break
    return (result, fish)

def move_shark(x, y, fish, grid, ate):
    global ans
    if ans < ate:
        ans = ate
    # 상어가 들어온 자리가 범위 내, 물고기가 있을 경우
    if 0 <= x < 4 and 0 <= y < 4 and grid[y][x][0] != 0:
        # 상어 방향
        d = grid[y][x][1] - 1
        dx = directions[d][0]
        dy = directions[d][1]
        fish.pop(grid[y][x][0])
        # 잡아먹음
        ate += grid[y][x][0]
        grid[y][x] = (0, grid[y][x][1])
        # rotate를 돌리고 -> 그 결과로 다시 move_shark
        for cnt in range(1, 4):
            rotated, new_fish = move_fish((x, y), fish.copy(), grid)
            move_shark(x + dx * cnt, y + dy * cnt, new_fish.copy(), rotated, ate)
    return

if __name__ == "__main__":
    # 방향, (x, y)
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    grid = []
    for i in range(4):
        temp = []
        data = list(map(int, input().split()))
        for i in range(0, 8, 2):
            temp.append((data[i], data[i+1]))
        grid.append(temp)
        
    # grid로부터 물고기 정보를 저장하는 dictionary를 만든다
    # fish는 살아있는 물고기 정보
    fish = dict()
    for i in range(4):
        for j in range(4):
            fish.update({grid[i][j][0]: (j, i)}) # i: (x, y)
    
    ans = 0
    move_shark(0, 0, fish, grid, 0)
    print(ans)
                
        