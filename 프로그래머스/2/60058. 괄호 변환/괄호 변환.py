def check_perfect(u):
    stack = []
    stack.append(u[0])
    for i in range(1, len(u)):
        if stack[-1] == '(' and u[i] == ')':
            stack.pop()
        else:
            stack.append(u[i])
    if stack:
        return False
    return True

def change(u):
    q = ''
    for i in range(1, len(u)-1):
        if u[i] == '(':
            q = q + ')'
        else:
            q = q + '('
    return q

def dfs(p):
    l_num = 0
    r_num = 0
    if p == '':
        return ''
    for i in range(len(p)):
        if p[i] == '(':
            l_num += 1
        else:
            r_num += 1
        if l_num == r_num:
            u = p[:i+1]
            v = p[i+1:]
            print('u, v is: ', u,' and ', v)
            if check_perfect(u):
                return u + dfs(v)
            else:
                return '(' + dfs(v) + ')' + change(u)
            
def solution(p):
    answer = ''
    answer = dfs(p)
            
    return answer