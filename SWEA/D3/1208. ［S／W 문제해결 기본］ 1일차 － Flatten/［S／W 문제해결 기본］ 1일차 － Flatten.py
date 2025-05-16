T = 10

for test_case in range(1, T+1):
    # 덤프 횟수 및 박스 높이
    N = int(input())
    lst = list(map(int, input().split()))
    
    lst.sort()
    
    for i in range(N):
        lst[-1] -= 1
        lst[0] += 1
        # 각 값을 앞, 뒤의 값과 비교
        for j in range(1, len(lst)):
            if lst[0] <= lst[j]:
                lst[0], lst[j-1] = lst[j-1], lst[0]
                break
                
        for j in range(len(lst)-2, -1, -1):
            if lst[-1] >= lst[j]:
                lst[-1], lst[j+1] = lst[j+1], lst[-1]
                break
                
        if (lst[-1] - lst[0]) <= 1:
            break
    ans = lst[-1] - lst[0]
    print(f'#{test_case} {ans}')