n = int(input())
cnt = 0
while n % 5 != 0 and n > 0:
    cnt += 1
    n -= 3
            
if n % 5 == 0 and n > 0:
    cnt += n // 5
    n %= 5
    
if n == 0:
    print(cnt)
else:
    print(-1)