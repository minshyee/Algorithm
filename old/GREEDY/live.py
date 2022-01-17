def solution(food_times, k):
    answer = -1
    i = -1
    l = len(food_times)
    while  k != 0:
        i += 1
        if i >= l:
            i %= l
        if food_times[i] != 0:
            food_times[i] -= 1
            k -= 1
    for i in range(l):
        if food_times[i] > 0:
            answer = i+1
            break
    return answer

def solution2(food_times, k):
    answer = -1
    i = 0
    ind = 0
    l = len(food_times)

    while  k != 0:
        if food_times[i] > 0:
            food_times[i] -= 1
            ind = i
            k -= 1
            # print(food_times)
        i += 1
        if i == l:
            i = 0
    # print(ind)
    if ind == l - 1:
        j = 0
    else:
        j = ind +1

    while food_times[j] == 0:
        if j == l-1:
            j = 0
        else:
            j += 1
    answer = j+1
    return answer

def solution3(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        return -1

    i = 0
    ind = 0
    l = len(food_times)
    b = [1]*l

    while  k != 0:
        if food_times[i] > 0:
            food_times[i] -= 1
            if food_times[i] == 0:
                b[i] = 0
            k -= 1
        i += 1
        if i == l:
            i = 0

    ind = i #마지막 연산 + 1 값
    try:
        answer = b[ind:].index(1) + ind + 1
    except:
        answer = b[:ind].index(1) + 1
    return answer
