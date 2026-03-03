import sys
from collections import deque

# from solution import init, add, remove, calculate
glb_N = 0
glb_K = 0

# 기차 운행 정보를 저장하는 dictionary {mid: (sid, eid, mInverval)}

# 서로 겹치는 역이 있는지(최대 공약수를 나누어봄)
def check_intersection(new, train):
    s1, e1, inter1, _, _ = train_info[new]
    s2, e2, inter2, _, _ = train_info[train]
    # 작은 쪽의 시작점을 큰 쪽 근처로 붙여, 반복 횟수를 줄일 수 있음
    if s1 < s2:
        s1 += ((s2 - s1) // inter1) * inter1
    else:
        s2 += ((s1 - s2) // inter2) * inter2

    # 범위가 넘어가지 않는 한
    while s1 <= e1 and s2 <= e2:
        # 만약 s1과 s2가 같은 값이라면
        if s1 == s2:
            return True
        elif s1 < s2:
            s1 += inter1
        else:
            s2 += inter2
    # 범위를 넘어가면 - 교차점이 없는 것
    return False

def init(N, K, mId, sId, eId, mInterval):
    global glb_N, glb_K, train_info
    glb_N = N
    glb_K = K
    train_info = {}
    # 개별 기차노선에 대해서
    for i in range(K):
        add(mId[i], sId[i], eId[i], mInterval[i])


def add(mId, sId, eId, mInterval):
    train_info[mId] = [sId, eId, mInterval, [], True]

    for train in train_info:
        if train!=mId and check_intersection(train, mId):
            train_info[train][3].append(mId)
            train_info[mId][3].append(train)



def remove(mId):
    train_info[mId][4] = False


def calculate(sId, eId):
	visited = set()
	queue = deque()

	# 역 기준으로 저장된 정보가 없으므로, 개별 열차를 조회해, 출발역 정차 가능 여부 확인
	for t in train_info:
		s, e, interval, _, activate = train_info[t]

		# 제거되지 않았고, 노선 범위 안에 있고, 실제로 정차할 수 있는지
		if activate and s <= sId <= e and (sId-s)%interval==0:
			queue.append((t, 0))
			visited.add(t)

	while queue:
		t, cnt = queue.popleft()

		# eId에 갈 수 있는지 계산
		s, e, interval, _, _ = train_info[t]
		if s <= eId <= e and (eId-s)%interval==0:
			# 출발, 도착 범위 내에 있으며 interval 간격 상 도달할 수 있는 역이라면
			return cnt

		# 도착역 eId에 도착하지 못했다면 환승을 고려함
		for nxt_t in train_info[t][3]:
			if nxt_t not in visited and train_info[nxt_t][4]:
				# 다음 환승할 열차가 방문한 적 없는 열차이고, 삭제되지 않았을 경우
				visited.add(nxt_t)
				queue.append((nxt_t, cnt+1))
	return -1

# system

CMD_INIT = 100
CMD_ADD = 200
CMD_REMOVE = 300
CMD_CALC = 400

def run():
    q = int(sys.stdin.readline())
    okay = False

    mIdArr = []
    sIdArr = []
    eIdArr = []
    mIntervalArr = []

    for i in range(q):
        inputarray = sys.stdin.readline().split()
        cmd = int(inputarray[0])

        if cmd == CMD_INIT:
            inputarray = sys.stdin.readline().split()
            n = int(inputarray[1])
            k = int(inputarray[3])
            for _ in range(k):
                tinfo = sys.stdin.readline().split()
                mIdArr.append(int(tinfo[1]))
                sIdArr.append(int(tinfo[3]))
                eIdArr.append(int(tinfo[5]))
                mIntervalArr.append(int(tinfo[7]))

            init(n, k, mIdArr, sIdArr, eIdArr, mIntervalArr)
            okay = True
        elif cmd == CMD_ADD:
            inputarray = sys.stdin.readline().split()
            mId = int(inputarray[1])
            sId = int(inputarray[3])
            eId = int(inputarray[5])
            mInterval = int(inputarray[7])
            add(mId, sId, eId, mInterval)
        elif cmd == CMD_REMOVE:
            inputarray = sys.stdin.readline().split()
            mId = int(inputarray[1])
            remove(mId)
        elif cmd == CMD_CALC:
            inputarray = sys.stdin.readline().split()
            sId = int(inputarray[1])
            eId = int(inputarray[3])
            ans = int(sys.stdin.readline().split()[1])
            ret = calculate(sId, eId)
            if ans != ret:
                okay = False
        else:
            okay = False

    return okay


if __name__ == '__main__':
    #sys.stdin = open('sample_input.txt', 'r')
    inputarray = sys.stdin.readline().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush = True)