"""
# SWEA D6 커피점&제과점

N개의 건물에 대해서, 0 ~ N-1 ID 값을 사용함
- 도로가 추가될 때, 거리 정보가 함께 주어짐
- M개 커피점, P개 제과점, 제한 거리 R
(커피점과 거리 차 <= R, 제과점과 거리 차 <= R)을 만족하며 각 거리 합이 최솟값인 경우
"""

import sys

import heapq, math

inf = math.inf

def init(N, K, sBuilding, eBuilding, mDistance):
    # 건물이 주어짐
    # 양방향 도로 정보가 주어짐 - 각 도로마다 연결된 2개의 건물 & 거리도 주어짐
    # 건물 간 도로의 길이는 고정되어 있고 - calcualate에서 커피점, 제과점, R 거리가 주어짐

    # 1. 건물 구조를 만듦
	global graph
	# graph = {}	# {start: {end:거리}}
	# * graph를 인접 리스트로 변경하자
	graph = [[] for _ in range(N)]

	global glb_N
	glb_N = N

	# for i in range(N):
	# 	# graph를 만듦
	# 	graph.update({i: {}})

    # 2. add를 통해서 도로를 만듦
	for k in range(K):
		add(sBuilding[k], eBuilding[k], mDistance[k])


def add(sBuilding, eBuilding, mDistance):
	# sBuilding -(mDistance)- eBuilding 건물을 연결하는 양방향 도로를 추가함

    # 1. 양쪽에서 서로 조회가 가능해야 함(dictionary OR 리스트)
	# * graph를 인접 리스트로 변경
	# graph[sBuilding].update({eBuilding: mDistance})
	# graph[eBuilding].update({sBuilding: mDistance})

	graph[sBuilding].append((eBuilding, mDistance))
	graph[eBuilding].append((sBuilding, mDistance))
	return


# 1. 별도의 dijkstra 함수를 만듦
# 2. graph로 dictionary를 구현해야 함
def dijkstra(numbers, start_points, restrict):
	'''

	:param start_points: 제과점 혹은 커피점 목록
	:return:
	'''
	# 0. 크기가 glb_N인 리스트를 생성하고, 이곳에 커피점, 제과점까지 주택에서부터의 거리 중 최솟값이 담김
	distances = [inf] * glb_N
	# 1. 멀티 소스이므로 입력받은 모든 []를 넣어야 함
	heap = []
	for i in range(numbers):
		start = start_points[i]
		# llist 상에서 거리 초기화 - start
		distances[start] = 0
		# 출발점 초기화(heap)
		heapq.heappush(heap, (0, start))

	while heap:
		dist, current = heapq.heappop(heap)
		# restrict 보다 큰 dist이거나
		# 현재 거리가 distances에 저장된 값보다 크면 지나감
		if dist > restrict or dist > distances[current]: continue

		# 현재 노드 기준 인접한 모든 노드에 대해 갱신 or 우선순위큐 삽입
		for next, weight in graph[current]:
			next_distance = dist + weight
			# * 조건 중요! next_distance가 restrict보다 작은 값일 때만 실행
			if next_distance < distances[next] and next_distance <= restrict:
				# * 다익스트라 내 업데이트 시점 중요! - 힙에 불필요한 중복 데이터 쌓임 방지
				distances[next] = next_distance
				heapq.heappush(heap, (next_distance, next))


	# 2. 만약 R의 범위를 넘어갈 경우 지나감
	# 이미 방문했을 경우 지나감
	# 값이 채워졌을 경우 지나감
	# 반환값이 list
	return distances

def calculate(M, mCoffee, P, mBakery, R):
    # 주택-커피점 거리 조회(최단 경로)
    # 주택-제과점 거리 조회(최단 경로)
    # 둘 다 만족하는 것들 중 합을 구해서 업데이트
    # 만약 커피점, 제과점 둘 다 R 이하인 주택이 없다면, -1 반환

	# 0. 커피점과 제과점으로부터의 거리를 저장할 리스트를 만듦
	global dist_from_coffee, dist_from_bakery

    # 1. 다중소스 다익스트라 - 각 거리를 저장함
	dist_from_coffee = dijkstra(M, mCoffee, R)
	# 저장된 값은 dist_from_coffee와 dist_from_bakery에 저장됨
	dist_from_bakery = dijkstra(P, mBakery, R)

	# 여기에 for문을 통해서 coffee점까지의 거리, bakery까지의 거리 중 합의 최솟값을 반환함
	res = 1000000

	for i in range(glb_N):
		C = dist_from_coffee[i]
		B = dist_from_bakery[i]
		# 1. 만약 mCoffee나 mBakery에 -1값이 있다면 X
		if C == 0 or B == 0:
			continue
		# 2. 만약 mCoffee나 mBakery에 inf 값이 있다면 X
		elif C == inf or B == inf:
			continue
		# 3. 만약 mCoffee + mBakery가 최솟값이면 갱신
		else:
			if C + B < res:
				res = C + B
	if res == 1000000:
		res = -1
	return res

# from solution import init, add, calculate

CMD_INIT = 100
CMD_ADD = 200
CMD_CALC = 300

def run():
	q = int(sys.stdin.readline())
	okay = False

	sBuildingArr = []
	eBuildingArr = []
	mDistArr = []

	for i in range(q):
		cmd = int(sys.stdin.readline())

		if cmd == CMD_INIT:
			inputarray = sys.stdin.readline().split()
			n = int(inputarray[0])
			k = int(inputarray[1])
			for _ in range(k):
				road = sys.stdin.readline().split()
				sBuildingArr.append(int(road[0]))
				eBuildingArr.append(int(road[1]))
				mDistArr.append(int(road[2]))

			init(n, k, sBuildingArr, eBuildingArr, mDistArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = sys.stdin.readline().split()
			sBuilding = int(inputarray[0])
			eBuilding = int(inputarray[1])
			mDist = int(inputarray[2])
			add(sBuilding, eBuilding, mDist)
		elif cmd == CMD_CALC:
			inputarray = sys.stdin.readline().split()
			m = int(inputarray[0])
			p = int(inputarray[1])
			r = int(inputarray[2])
			mCoffee = []
			for _ in range(m):
				mCoffee.append(int(sys.stdin.readline()))
			mBakery = []
			for _ in range(p):
				mBakery.append(int(sys.stdin.readline()))

			ans = int(sys.stdin.readline())
			ret = calculate(m, mCoffee, p, mBakery, r)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('input.txt', 'r')
	inputarray = sys.stdin.readline().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)