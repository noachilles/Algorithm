def solution(answers):
    N = 5
    L = len(answers)

    first = [i for i in range(1, N+1)]
    second = []
    for i in (1, 3, 4, 5):
        second += [2]
        second += [i]
    third = []
    for i in (3, 1, 2, 4, 5):
        third += [i] * 2
    
    L_f = len(first)
    L_s = len(second)
    L_t = len(third)

    scores = [0, 0, 0]

    for i in range(L):
        if answers[i] == first[i%L_f]:
            scores[0] += 1
        if answers[i] == second[i%L_s]:
            scores[1] += 1
        if answers[i] == third[i%L_t]:
            scores[2] += 1
    
    answer = []
    maximum = 0
    for i in range(3):
        if scores[i] > maximum:
            maximum = scores[i]
    
    for j in range(3):
        if scores[j] == maximum:
            answer.append(j+1)

    return answer