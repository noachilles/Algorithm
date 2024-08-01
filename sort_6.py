# 이코테 실전 6-2

# 입력
# (학생 수, N)
# (학생 이름 A, 학생 성적-정수 B)
# 출력
# 성적 낮은 순으로 출력

n = int(input())

std_d = []
for i in range(n):
    input_data = input().split()
    std_d.append((input_data[0], int(input_data[1])))

std_d = sorted(std_d, key = lambda student: student[1])
    
for _ in std_d:
    print(_[0], end=' ')
