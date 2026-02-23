# 냄새를 뿌리기
def update_scent():
	del_lst = []
	for i in shark_scent:
		if shark_scent[i][1] - 1 == 0:
			del_lst.append(i)
		else:
			shark_scent[i] = (shark_scent[i][0], shark_scent[i][1]-1)
		# 모든 냄새 1씩 감소 - 0이 되면 사라짐
	for j in del_lst:
		shark_scent.pop(j)
 
	for num in shark_now:
		x, y = shark_now[num]
		# 다시 돌아오더라도 K로 업데이트
		shark_scent.update({(x, y): (num, K)})

# 동일한 칸으로 들어가는 건 따로 처리해줘야 한다

def move_shark():
	# 2. 상어가 각자의 우선순위에 알맞는 위치로 이동
	for num in sorted(shark_now): # 각 살아있는 상어에 대해
		x, y = shark_now[num] # 현재 위치
		d = shark_d[num] # 현재 방향
		move = False
		# 우선순위 방향대로 빈 공간을 살핀다
		for i in range(4):
			n_d = priority[num][d-1][i]
			# print((num, d, n_d))
			nx, ny = x + directions[n_d-1][0], y + directions[n_d-1][1]
			# 만약 n_d 방향에 빈 칸이 있다면
			if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in shark_scent:
				shark_now[num] = (nx, ny)
				# 방향을 바꿔준다
				shark_d[num] = n_d
				move = True
				break
		# 주변에 빈 칸이 없었다면
		if not move:
			for i in range(4):
				n_d = priority[num][d-1][i]
				nx, ny = x + directions[n_d-1][0], y + directions[n_d-1][1]
				if 0 <= nx < N and 0 <= ny < N and (nx, ny) in shark_scent:
					if shark_scent[(nx, ny)][0] == num:
						shark_now[num] = (nx, ny)
						shark_d[num] = n_d
						move = True
						break

def chk_same():
	del_lst = []
	for least in sorted(shark_now):
		for big in range(least+1, M+1):
			if big not in shark_now:
				continue
			else: 
				if shark_now[least] == shark_now[big]:
					del_lst.append(big)
	for i in set(del_lst):
		shark_now.pop(i)

# 상어가 1마리인지 확인
def chk_one():
	if len(shark_now) == 1:
		return True
	return False

def main():
	# 풀이
	# 1. 최초 위치에 냄새를 뿌린다
	for t in range(1, 1001):
		move_shark()
		chk_same()
		chk = chk_one()
		update_scent()
		if chk:
			return t
	return False

if __name__ == "__main__":
	chk = False
    
	shark_now = dict()
	shark_scent = dict() # (x, y): (number, k)
	directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # (0~3)

	N, M, K = map(int, input().split())
	grid = [list(map(int, input().split())) for _ in range(N)]
	shark_d = [0] + list(map(int, input().split()))
	priority = dict()
	for num in range(1, M+1):
		data = []
		for i in range(4):
			data.append(list(map(int, input().split())))
		priority.update({num: data})
		

	for i in range(N):
		for j in range(N):
			if 1 <= grid[i][j] <= M:
				shark_scent.update({(j, i): (grid[i][j], K)})
				shark_now.update({grid[i][j]: (j, i)})
	chk = main()
	if chk:
		print(chk)
	else:
		print(-1)