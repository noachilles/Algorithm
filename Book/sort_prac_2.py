# sort 실전 문제 2
# 입력
# 학생 수 n
# 두 번째 ~ (n+1)번째 : 학생 이름-a 성적-b
# 출력
# 성적이 낮은 순으로 학생 이름 출력

n = int(input())
students = []
for i in range(n):
    input_data = input().split()
    students.append((input_data[0], int(input_data[1])))

# 점수를 기준으로 정렬하기 위해서 key를 사용
# dictionary로 하니까 sorted 함수 사용이 어렵네, 간단한 문제이니 tuple을 사용하도록 하자.
array = sorted(students, key=lambda x: x[1])

# 결과 역시 튜플로 나옴
for student in array:
    print(student[0], end=' ')
