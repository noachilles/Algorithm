T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    mx = N-1
    ans = 0

    for i in range(N-1, -1, -1):
        if lst[i] < lst[mx]:
            ans += (lst[mx] - lst[i])
        else:
            mx = i
    print(ans)