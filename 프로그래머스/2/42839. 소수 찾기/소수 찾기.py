from itertools import permutations

def solution(numbers):
    L = len(numbers)
    answer = 0
    visited = set()
    # 1. 모든 조합으로 수를 만들어야 함
    # 1) 조합으로 문자열을 만들어야 함
    for i in range(1, L+1):
        combinations_list = []
        for comb in permutations(numbers, i):
            # 2) 문자열을 수로 만들어야 함
            num = int("".join(map(str, comb)))
            if num not in visited:
                combinations_list.append(num)
                visited.add(num)
        # 2. 각 조합의 수에 대한 소수 판별이 필요함
        for number in combinations_list:
            # 1) 일단 1이 아니어야 함   
            if number <= 1:
                continue
            # 2) 1 말고는 나누어지는 수가 없어야 함
            else:
                flag = True
                for j in range(2, number):
                    if number % j == 0:
                        flag = False
                        break
                if flag:
                    answer += 1
    return answer