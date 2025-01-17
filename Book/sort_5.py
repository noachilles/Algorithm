# 이코테 실전 6-1

# 입력 
# (수열에 속한 수의 개수, N)
# (수열에 속한 수, N개)
# 출력
# 내림차순 정렬 결과 end=' '

n = int(input())
lst = [int(input()) for i in range(n)]

lst = sorted(lst, reverse=True)
print(*lst)