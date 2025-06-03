T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    mx = N-1
    ans = 0

    for i in range(N-1, -1, -1):
        if lst[i] > lst[mx]:
            for j in range(i+1, mx, 1):
                ans += (lst[mx] - lst[j])
            mx = i
    for i in range(mx):
        ans += (lst[mx] - lst[i])
    print(ans)