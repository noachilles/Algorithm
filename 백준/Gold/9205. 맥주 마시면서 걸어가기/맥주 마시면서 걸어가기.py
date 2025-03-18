from collections import deque

def bfs():
    global visited, dest, festx, festy
    q = deque()
    q.append((homex, homey))
    while q:
        nowx, nowy = q.popleft()
        if nowx == festx and nowy == festy:
            return True
        for i in range(n+1):
            if not visited[i]:
                cx, cy = dest[i]
                # 갈 수 있는 편의점 또는 락페에 대해
                if abs(cx - nowx) + abs(cy - nowy) <= 50 * 20:
                    q.append((cx, cy))
                    visited[i] = True
    return False

if __name__ == "__main__":
    
    t = int(input())
    k = t
    while t > 0:
        dest = []
        n = int(input())
        home = [tuple(map(int, input().split()))]
        # 편의점
        for i in range(n):
            dest.append(tuple(map(int, input().split())))
        dest.append(tuple(map(int, input().split())))
         
        visited = [False] * (n + 1)
        
        # 페스티벌, 집 좌표와 거리
        festx, festy = dest[-1]
        homex, homey = home[0]
        dist = abs(festx - homex) + abs(festy - homey)
        
        # 집에서 락페까지 다이렉트로 갈 수 있다면
        if dist <= 50 * 20:
            print('happy')
            
        else:
            if bfs():
                print('happy')
                
            else:
                print('sad')
                
        t -= 1