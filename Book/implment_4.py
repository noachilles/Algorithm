# 이코테 실전문제 4-2

# 입력
# (맵의 세로 크기 N, 가로 크기 M)
# (캐릭터가 있는 칸의 좌표 (A, B), 방향 d)
# 0: 북쪽 1: 동쪽 2: 남쪽 3: 서쪽
# (맵이 육지인지 바다인지에 대한 정보 N개의 줄에 북 -> 남, 서 -> 동)
# 출력
# 캐릭터가 방문한 칸의 수  

# 캐릭터는 바라보고 있는 방향의 왼쪽부터 갈 수 있는 칸(가보지 않았으며 육지인 칸)을 탐색  
# 만약 왼쪽 칸은 방문했다면 회전만 진행하고 똑같은 작업을 반복 수행
# 모든 칸으로 이동할 수 없다면 움직임을 멈춤 -> 종료  
# +++
# turn_time 변수를 사용해 해결
# 모든 방향이 막혀 있고 한 칸 뒤에 육지가 있다면 뒤로 한 칸 이동하는 조건을 깜빡함

n, m = map(int, input().split())
x, y, d = map(int, input().split())
gmap = [list(map(int,input().split())) for _ in range(n)]
been = [[0 for i in range(m)] for j in range(n)]
side = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
count = 1

def turn_left(d):
    d -= 1
    if d == -1:
        d = 3
    return d

turn_time = 0
nd = d
while True:
    been[x][y] = 1
    nd = turn_left(nd)
    turn_time += 1
    chk = (gmap[x+side[nd][0]][y+side[nd][1]] or been[x+side[nd][0]][y+side[nd][1]])
    print('now: gmap[{}, {}]\nnd = {}\ncheck = {}'.format(x, y, nd, chk))
    if chk == 0:
        # 전진 내용
        x += side[nd][0]
        y += side[nd][1]
        d = nd
        count += 1
        turn_time = 0
    else:

        if turn_time == 4:
            nx = x - side[nd][0]
            ny = y - side[nd][1]
            if gmap[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
print(count)
        
