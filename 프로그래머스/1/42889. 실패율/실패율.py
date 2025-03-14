from collections import Counter

def solution(N, stages):
    answer = []
    cnt = Counter(stages)
    through = [0] * (N+1)
    d = dict()
    for i in range(1, N+1):
        d[i] = 0
    for i in range(1, N+1):
        if i in cnt:
            d[i] += cnt[i]
        for j in cnt:
            if i < j:
                d[i] += cnt[j]
        if d[i] != 0:
            d[i] = (cnt[i] / d[i])
    answer = sorted(d, key=lambda x: d[x], reverse=True)
    return answer