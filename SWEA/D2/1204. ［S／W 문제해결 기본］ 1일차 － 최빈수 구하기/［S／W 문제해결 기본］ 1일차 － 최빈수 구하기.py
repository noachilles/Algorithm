T = int(input())
for test_case in range(1, T+1):
    case_number = int(input())
    data = list(map(int, input().split()))[:1000]
    dictionary = dict()
    for i in data:
        if i not in dictionary:
            dictionary.update({i: 1})
        else:
            dictionary[i] += 1
    item_lst = sorted(dictionary.items(), key=lambda x: (-x[1], -x[0]))
    print(f'#{case_number} {item_lst[0][0]}')