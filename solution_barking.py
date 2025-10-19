# boj 13414

'''
1. 수강신청 버튼 활성화 이후 -> 수강신청 버튼을 조금이라도 빨리 누른 학생 - 대기목록에 먼저 들어감
2. 이미 대기열에 들어가있는 상태에서 다시 수강신청 버튼 -> 맨 뒤로
3. 수강신청 버튼 비활 -> 대기목록 앞에서부터 수강신청 완료 / 인원 꽉: 대기목록 무시
=> 최종 수강신청 성공 인원을 출력하라

입력
K, L: 수강 가능 인원, 대기목록 길이
L줄: 수강신청 버튼 클릭한 학생 학번(8자리 숫자)
'''
# import sys
# input=sys.stdin.readline
#
# K, L = map(int, input().split())
# student_lst = dict()
# i = 1
# for _ in range(L):
#     student_id = input()
#     if student_id in student_lst:
#         student_lst.pop(student_id)
#     # 없으면 -> 그대로 등록
#     student_lst[student_id] = i
#
# # 만약 수강 가능 인원이 대기목록보다 크거나 같다면 - 전체 출력
# # 아닐 경우 자름
# l = L
# if K < L:
#     l = K
#
# possible = list(student_lst.keys())[:l]
# for student_id in possible:
#     print(student_id, end='')

# boj 17219
'''
이미 저장된 사이트 주소만 입력됨
사이트 주소, 비밀번호 입력 받음
'''
# N, M = map(int, input().split())
#
# site_dict = dict()
#
# for _ in range(N):
#     site, pw = input().split()
#     site_dict[site] = pw
#
# for _ in range(M):
#     site = input()
#     print(site_dict[site])

# boj 9375
'''
T는 최대 100
의상 최대 30
의상 이름 / 의상 종류 공백 구분
만약 모든 의상이 종류가 다르다고 하면  
Combinations(30, 1~30)
한 개 고르는 경우, 두 개 고르는 경우... n개 고르는 경우

핵심: combination을 하나씩 구하면 O(2^N*N)으로 시간초과 => 경우의 수로 구하자!
모자 3개 - 모자1, 모자2, 모자3, 모자 쓰지 X
상의 2개 - 상의1, 상의2, 상의 X
'''

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     # 해빈이의 옷장
#     closet = dict()
#     for _ in range(n):
#         name, type = input().split()
#         if type in closet:
#             closet[type] += 1
#         # 입는다, 입지 않는다 2개의 경우의 수
#         else:
#             closet[type] = 2
#
#     types = len(closet)
#
#     res = 1
#     for k in closet.values():
#         res *= k
#     # 아무것도 입지 않는 경우의 수 1을 빼줌
#     print(res - 1)

# boj - 21939
'''
recommend x)  
x=1: 가장 어려운 문제 번호 출력 - 여러 개이면 문제 번호 큰 것으로 출력
x=-1: 가장 쉬운 문제 번호 출력 - 여러 개이면 문제 번호 작은 것으로 출력

add P L)
문제 리스트에 난이도가 L인 문제 번호 P를 추가 - 리스트 내 중복은 X

solved P)
추천 문제 리스트에서 P 제거

단순 이진 탐색으로는 풀 수 없나?
- 만약 모든 문젝 동일한 난이도를 갖고 있다면 N/2까지 찾을 수도
logN만에 찾을 수 있다는 장점이 있음
key를 두 개 가져야 하나?
만약 작은 값을 찾는다면 난이도가 제일 작은 것 중, 더 작은 문제 번호
큰 값을 찾는다면 난이도가 제일 큰 것 중, 더 큰 문제 번호
순서대로 우선순위 1, 2

풀고 나서 알게 된 것
* tuple을 사용하면 일일이 비교하지 않아도 Python이 우선순위 비교를 해줌
* 클래스를 사용하지 않고 BST를 진행하는 방법도 볼 필요가 있음 - 오히려 시간도 오래 걸림
* heapq를 주로 사용해서 문제를 풀이한 것으로 보임
'''
#
# # Node로 BST를 먼저 만듦
# class Node:
#     def __init__(self, p, l):
#         self.key = (p, l)
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, p, l):
#         if self.root is None:
#             self.root = Node(p, l)
#         else:
#             self._insert(self.root, p, l)
#     def _insert(self, node, p, l):
#         # 난이도 (L)에 대해 먼저 대소비교하며
#         # L이 같다면 문제 번호 비교
#         if l < node.key[1]:
#             if node.left is None:
#                 node.left = Node(p, l)
#             else:
#                 self._insert(node.left, p, l)
#         elif l > node.key[1]:
#             if node.right is None:
#                 node.right = Node(p, l)
#             else:
#                 self._insert(node.right, p, l)
#         else:
#             # 다음으로는 문제번호가 작을 경우
#             if p < node.key[0]:
#                 if node.left is None:
#                     node.left = Node(p, l)
#                 else:
#                     self._insert(node.left, p, l)
#             else:
#                 if node.right is None:
#                     node.right = Node(p, l)
#                 else:
#                     self._insert(node.right, p, l)
#
#     def search(self, x):
#         node = self.root
#         # 왼쪽으로 내려가는 경우
#         if x < 0:
#             # left가 있는 동안
#             while node.left is not None:
#                 node = node.left
#         # 오른쪽으로 내려가는 경우
#         else:
#             # right가 있는 동안
#             while node.right is not None:
#                 node = node.right
#         return node.key
#
#     def delete(self, p, l):
#         self.root = self._delete(self.root, p, l)
#
#     def _delete(self, node, p, l):
#         if node is None:
#             return node
#
#         if l < node.key[1]:
#             node.left = self._delete(node.left, p, l)
#         elif l > node.key[1]:
#             node.right = self._delete(node.right, p, l)
#         else:
#             if p < node.key[0]:
#                 node.left = self._delete(node.left, p, l)
#             elif p > node.key[0]:
#                 node.right = self._delete(node.right, p, l)
#             else:
#                 if node.left is None:
#                     return node.right
#                 elif node.right is None:
#                     return node.left
#
#                 temp = self._minValueNode(node.right)
#                 node.key = temp.key
#                 node.right = self._delete(node.right, temp.key[0], temp.key[1])
#
#         return node
#
#     def _minValueNode(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left  # 왼쪽 자식이 없을 때까지 이동하여 최소값 노드를 찾음
#         return current
#
#
# # 문제 리스트
# riddle_dict = dict()
# bst = BST()
#
# N = int(input())
# for _ in range(N):
#     P, L = map(int, input().split())
#     bst.insert(P, L)
#     riddle_dict[P] = L
#
# M = int(input())
# for _ in range(M):
#     # 명령문 입력
#     data = input().split()
#     if data[0] == 'add':
#         p, l = map(int, data[1:3])
#         bst.insert(p, l)
#         riddle_dict[p] = l
#     elif data[0] == 'recommend':
#         x = int(data[1])
#         riddle = bst.search(x)
#         print(riddle[0])
#     else:
#         p = int(data[1])
#         bst.delete(p, riddle_dict[p])
#         del riddle_dict[p]

# boj - 14888

'''
N개의 수로 이루어진 수열 A_1, A_2, ..., A_N이 주어짐
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자
- 우선 순위 무시, 앞에서부터 진행
- 나눗셈은 정수 나눗셈으로, 몫만 취함
만들 수 있는 식의 결과가 최대인 것과 최소인 것

앞에서부터 연산을 해야하며, 연산자의 개수도 정해져있음 -> 재귀 형식으로 풀자
'''

# # 함수: 최종 순서가 정해지면 앞에서부터 연산을 수행함
# visited = set()
#
# def f(idx, s, m, t, d, res):
#     global res_max, res_min
#     # 만약 이미 조회한 적이 있다면 return
#     if (s, m, t, d, res) in visited:
#         return
#     if idx == N:
#         res_max = max(res_max, res)
#         res_min = min(res_min, res)
#         return
#     visited.add((s, m, t, d, res))
#     # 그렇지 않다면 앞에서부터 연산을 수행함
#     # idx는 1부터 시작해야 하며, res는 기본 A_list[0]
#     if s > 0:
#         # 덧셈이 있을 경우
#         f(idx+1, s-1, m, t, d, res+A_list[idx])
#     if m > 0:
#         # 뺄셈이 남아있을 경우
#         f(idx+1, s, m-1, t, d, res-A_list[idx])
#     if t > 0:
#         # 곱셈이 남아있을 경우
#         f(idx+1, s, m, t-1, d, res*A_list[idx])
#     if d > 0:
#         # 나눗셈이 남아있을 경우
#         f(idx+1, s, m, t, d-1, int(res/A_list[idx]))
#
#
# N = int(input())
# A_list = list(map(int, input().split()))
# res_max = -10**(13)
# res_min = 10**(13)
# # 각 연산자의 수를 아래와 같이 나눔
# s, m, t, d = list(map(int, input().split()))
# f(1, s, m, t, d, A_list[0])
# print(res_max)
# print(res_min)

# boj - 14889

'''
N명의 사람, N은 짝수
N/2명으로 이루어진 스타트팀 / 링크팀

능력치 S_ij는 i번, j번이 같은 팀에 속했을 때, 팀에 더해지는 능력치  
팀의 능력치: 팀에 속한 모든 쌍의 능력치 S_ij의 합
S_ij != S_ji
team(i, j) = S_ij + S_ji

팀의 능력치 차이를 최소로
(1, 4), (2, 3) => 6, 6

S)  
문제를 풀이하려면, 모든 조합의 쌍을 구해야 함
단, (1, 4)를 선택한 경우와 (2, 3)을 선택한 경우는(예시에서) 같으므로
굳이 두 번을 해줄 필요 X
이 점을 생각해서 들어가자
N <= 20이므로 크지 X

'''

# # 경험치를 저장할 리스트
# ex_list = []
# # combinations는 조합을 구하고, 경험치 연산까지 수행
# def combinations(start, n, arr):
#     if len(arr) == n:
#         # 경험치 연산
#         ex = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 a, b = arr[i], arr[j]
#                 ex += (each_score[a][b] + each_score[b][a])
#         ex_list.append(ex)
#     for i in range(start, N):
#         combinations(i+1, n, arr+[i])
#
# # input
# N = int(input())
#
# each_score = []
# for _ in range(N):
#     each_score.append(list(map(int, input().split())))
#
# # 반환할 결과: output
# res = float('inf')
# # 모든 조합에 대한 경험치를 구함
# combinations(0, N//2, [])
#
# # ex_list에 대해, 좌우 각 끝이 서로소
# # 두 조합의 경헙치 차를 구해서 비교함
# l = len(ex_list)
# for i in range(l):
#     j = l - 1 - i
#     if j <= i:
#         break
#     res = min(res, abs(ex_list[i] - ex_list[j]))
# print(res)

# boj - 1927

'''
1. 배열에 자연수 x 넣음
2. 배열에서 가장 작은 값 출력, 제거 - pq의 pop
'''

# # priority queue 만들기
# import heapq
# import sys
#
# input = sys.stdin.readline
#
# pq = []
#
# N = int(input())
# for _ in range(N):
#     x = int(input())
#     if x > 0:
#         heapq.heappush(pq, x)
#     # x가 0이면 배열에서 가장 작은 값 출력, 값을 배열에서 제거
#     else:
#         if pq:
#             print(heapq.heappop(pq))
#         else:
#             print(0)

# boj - 2075

'''
NxN 표에 수 N^2 개  
모든 수는 자신의 한 칸 위에 있는 수보다 큼
N번째 큰 수를 찾는 프로그램 작성 & 표에 채워진 수는 모두 다름

그냥 전부 다 넣고, 우선순위 큐 pop N번 돌리기
=> 메모리 초과 => 입력되는 N개의 수에 대해서, heapq[0]보다 작은 경우, 활용하지 않음
'''
import heapq

N = int(input())

board = []
# N개씩 처리함
# 첫번째 처리 시: 일단 N개를 모두 넣음
start_list = list(map(int, input().split()))
for i in start_list:
    heapq.heappush(board, i)
# 그 다음부터, board의 [0]: 최소값과 비교해 더 작은 값이면 무시, 더 큰 값이면 넣고 heappop()
for _ in range(N-1):
    input_list = list(map(int, input().split()))
    for i in input_list:
        if i > board[0]:
            heapq.heappush(board, i)
            heapq.heappop(board)

# 이까지 모두 끝내면, board에는 N개의 큰 값들만 들어있음
print(heapq.heappop(board))