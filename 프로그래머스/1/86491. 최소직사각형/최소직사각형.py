def solution(sizes):
    mi, ma = 1, 1
    for r, c in sizes:
        if r < c:
            if mi < r:
                mi = r
            if ma < c:
                ma = c
        elif c < r:
            if mi < c:
                mi = c
            if ma < r:
                ma = r
        else:
            if mi < c:
                mi = c
            if ma < r:
                ma = r
    answer = mi * ma
    return answer