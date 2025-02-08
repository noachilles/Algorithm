def solution(s):
    answer = 0
    
    
    # 기능을 하나씩 구현해보자
    # 문자를 1개씩 자르면
    # print(len(s))
    min_s = len(s)
    
    for n in range(1, (len(s)) // 2 + 1):
        # print(f'when n = {n}: ')
        len_s = len(s)
        cnt = dict()
        # 이전에도 같은 값이었는지 판단
        pre = False
        now = False

        for i in range(n, len(s) + 1, n):
            cnt[s[i - n : i]] = 1
        
        for i in range(2 * n, len(s) + 1, n):
            if s[(i - 2 * n):(i - n)] == s[(i - n):i]:
                cnt[s[i-n : i]] += 1
                len_s -= n
                now = True
                if cnt[s[i-n : i]] > 1 and pre == False:
                    len_s += 1
                if cnt[s[i-n : i]] == 10:
                    len_s += 1
                if cnt[s[i-n : i]] == 100:
                    len_s += 1
                if cnt[s[i-n : i]] == 1000:
                    len_s += 1
            else:
                now = False
                cnt[s[i-n : i]] = 1
            # print(cnt)
            
            pre = now
            
        if len_s < min_s:
            min_s = len_s
    answer = min_s
    
    return answer