data = input().split('-')
res = []

for small in data:
    if '+' in small:
        temp_res = small.split('+')
        temp_ans = int(temp_res[0])
        for i in range(1, len(temp_res)):
            temp_ans += int(temp_res[i])
        res.append(temp_ans)
    else:
        res.append(int(small))

ans = res[0]
for i in range(1, len(res)):
    ans -= res[i]
print(ans)