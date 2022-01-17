def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    d = list(filter(lambda x : x in reserve, lost))
    for j in d:
        reserve.remove(j)
        lost.remove(j)
    answer = n - len(lost)
    ind = 0

    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
        else:
            continue

    return answer
