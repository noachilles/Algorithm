import sys
input = sys.stdin.readline

s = input().rstrip()
# 일반 문자도 포함되어 있다는 사실을 간과했다
# 문자열에서 in을 하면 성능이 좋지 않을 것 같은데
# 2개 혹은 3개로 묶어서 cnt할 문자들을 먼저 cnt

def chk(s): # dz, z 제외 크로아티아 알파벳 찾고 개수 세기
    cnt = 0
    for i in range(len(s)-1):
        if s[i:i+2] == None:
            break
        elif s[i:i+2] in d:
            cnt += 1
            visited.append(i)
            visited.append(i+1)
    return cnt

def chk_dz(s): # dz 찾고 개수 세기
    cnt = 0
    for i in range(len(s)-2):
        if s[i:i+3] == None:
            break
        elif s[i:i+3] == 'dz=':
            cnt += 1
            visited.append(i)
            visited.append(i+1)
            visited.append(i+2)
    return cnt

def chk_z(s): 
    cnt = 0
    for i in range(len(s)-1):
        temp = set(visited)
        if i not in temp:
            if s[i:i+2] == None:
                break
            elif s[i:i+2] == 'z=':
                visited.append(i)
                visited.append(i+1)
                cnt += 1
    return cnt

def chk_else(s):
    cnt = 0
    for i in range(len(s)):
        if not i in visited:
            cnt += 1
    return cnt

if __name__ == '__main__':
    cnt = 0
    d = {'c=':0, 'c-':0, 'd-':0, 'lj':0, 'nj': 0, 's=':0}
    visited = []
    cnt += chk(s)
    cnt += chk_dz(s)
    cnt += chk_z(s)
    visited = set(visited)
    cnt += chk_else(s)    
    print(cnt)
    