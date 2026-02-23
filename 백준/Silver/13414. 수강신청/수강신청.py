'''
1. 수강신청 버튼 활성화 이후 -> 수강신청 버튼을 조금이라도 빨리 누른 학생 - 대기목록에 먼저 들어감
2. 이미 대기열에 들어가있는 상태에서 다시 수강신청 버튼 -> 맨 뒤로
3. 수강신청 버튼 비활 -> 대기목록 앞에서부터 수강신청 완료 / 인원 꽉: 대기목록 무시
=> 최종 수강신청 성공 인원을 출력하라

입력
K, L: 수강 가능 인원, 대기목록 길이
L줄: 수강신청 버튼 클릭한 학생 학번(8자리 숫자)
'''
import sys
input=sys.stdin.readline

K, L = map(int, input().split())
student_lst = dict()
i = 1
for _ in range(L):
    student_id = input()
    if student_id in student_lst:
        student_lst.pop(student_id)
    # 없으면 -> 그대로 등록
    student_lst[student_id] = i

# 만약 수강 가능 인원이 대기목록보다 크거나 같다면 - 전체 출력
# 아닐 경우 자름
l = L
if K < L:
    l = K

possible = list(student_lst.keys())[:l]
for student_id in possible:
    print(student_id, end='')