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
'''

# Node로 BST를 먼저 만듦
class Node:
    def __init__(self, p, l):
        self.key = (p, l)
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, p, l):
        if self.root is None:
            self.root = Node(p, l)
        else:
            self._insert(self.root, p, l)
    def _insert(self, node, p, l):
        # 난이도 (L)에 대해 먼저 대소비교하며
        # L이 같다면 문제 번호 비교
        if l < node.key[1]:
            if node.left is None:
                node.left = Node(p, l)
            else:
                self._insert(node.left, p, l)
        elif l > node.key[1]:
            if node.right is None:
                node.right = Node(p, l)
            else:
                self._insert(node.right, p, l)
        else:
            # 다음으로는 문제번호가 작을 경우
            if p < node.key[0]:
                if node.left is None:
                    node.left = Node(p, l)
                else:
                    self._insert(node.left, p, l)
            else:
                if node.right is None:
                    node.right = Node(p, l)
                else:
                    self._insert(node.right, p, l)

    def search(self, x):
        node = self.root
        # 왼쪽으로 내려가는 경우
        if x < 0:
            # left가 있는 동안
            while node.left is not None:
                node = node.left
        # 오른쪽으로 내려가는 경우
        else:
            # right가 있는 동안
            while node.right is not None:
                node = node.right
        return node.key

    def delete(self, p, l):
        self.root = self._delete(self.root, p, l)

    def _delete(self, node, p, l):
        if node is None:
            return node

        if l < node.key[1]:
            node.left = self._delete(node.left, p, l)
        elif l > node.key[1]:
            node.right = self._delete(node.right, p, l)
        else:
            if p < node.key[0]:
                node.left = self._delete(node.left, p, l)
            elif p > node.key[0]:
                node.right = self._delete(node.right, p, l)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self._minValueNode(node.right)
                node.key = temp.key
                node.right = self._delete(node.right, temp.key[0], temp.key[1])

        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left  # 왼쪽 자식이 없을 때까지 이동하여 최소값 노드를 찾음
        return current


# 문제 리스트
riddle_dict = dict()
bst = BST()

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    bst.insert(P, L)
    riddle_dict[P] = L

M = int(input())
for _ in range(M):
    # 명령문 입력
    data = input().split()
    if data[0] == 'add':
        p, l = map(int, data[1:3])
        bst.insert(p, l)
        riddle_dict[p] = l
    elif data[0] == 'recommend':
        x = int(data[1])
        riddle = bst.search(x)
        print(riddle[0])
    else:
        p = int(data[1])
        bst.delete(p, riddle_dict[p])
        del riddle_dict[p]
