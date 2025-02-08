# 프로그래머스 - 문자열 압축(Lv.2)

# 처음에는 1개, 2개, 3개...씩 잘라서 dictionary에 key로 넣고 value를 더해주는 방법을 사용했다.
# value를 더하는 과정에서 연산 오류가 생겨 실패 - 정확도는 51정도 됐다

def solution(s):
    answer = 0
    
    min_s = len(s)
    
    for n in range(1, (len(s)) // 2 + 1):
        len_s = len(s)
        # 이전에도 같은 값이었는지 판단
        cnt = dict()
        for i in range(n, len(s) + 1, n):
            cnt[s[i - n: i]] = 1
            for i in range(2 * n, len(s) + 1, n):
                if s[(i - 2 * n):(i - n)] == s[(i - n):i]:
                    cnt[s[i-n:i]] += 1
                
        for k, v in cnt.items():
            # v가 2번 이상 반복되면
            if v > 1:
                # n(자릿수) * (v(반복 횟수) - 1(하나만 남겨둠))을 빼고
                len_s -= n * (v - 1)
                len_s += 1
        print('len is ', len_s)
        if len_s < min_s:
            min_s = len_s
    answer = min_s
    
    return answer

# version 2.
# 틀린 이유를 찾는 게 어려웠는데, 10개가 되면 두 자리가 늘어나기 때문이다.
def solution(s):
    answer = 0
    min_s = len(s)
    
    for n in range(1, (len(s)) // 2 + 1):
        len_s = len(s)
        # 이전에도 같은 값이었는지 판단
        pre = False
        now = False
        for i in range(2 * n, len(s) + 1, n):
            cnt = 1
            if s[(i - 2 * n):(i - n)] == s[(i - n):i]:
                len_s -= n
                cnt += 1
                now = True
                if cnt > 1 and pre == False:
                    len_s += 1
            else:
                now = False
            pre = now
            
        if len_s < min_s:
            min_s = len_s
    answer = min_s
    
    return answer

# version 3. 2자리 숫자에 대한 대비가 안 된다고... 
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
                if cnt[s[i-n : i]] > 9:
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

# 최종 코드 - 10, 100, 1000(최초로 자릿수가 바뀌는 경우에 대해서만 추가 자리 1을 늘렸다.)
# 코드가 되게 효율적이거나 깔끔하지는 않아서 아쉬운 마음이 있으나 시간을 많이 들인 만큼 결과가 나와서 다행이다.
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