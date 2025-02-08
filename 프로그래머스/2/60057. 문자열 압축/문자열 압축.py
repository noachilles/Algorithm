def solution(s):
    answer = 0
    min_s = len(s)
    
    for n in range(1, (len(s)) // 2 + 1):
        len_s = len(s)
        cnt = dict()
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
            pre = now
            
        if len_s < min_s:
            min_s = len_s
    answer = min_s
    
    return answer