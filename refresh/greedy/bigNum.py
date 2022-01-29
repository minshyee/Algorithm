n, m, k = map(int, input().split())
lst = sorted(list(map(int, input().split())),reverse=True)
total = 0 # 총 합
idx = 0
prev = 0 # 연속 횟수

# print(lst)
while m != 0: # 총 더할 횟수
    # print('m',m, 's',total)
    if k == prev: # 연속 횟수가 최대 연속 가능 수와 같으면
        total += lst[int(not(idx))]  # 두번째 큰수를 한번 더한다
        # print('+',lst[int(not(idx))])
        prev = 0 # 연속 횟수 초기화
    else:
        total += lst[idx] # 아닐경우, 연속 가능 횟수만큼 최대값 더하기
        # print(lst[idx])
        prev += 1 # 연속 횟수 증가
    m -= 1 # 더하기 연산 수 감소
print(total)
