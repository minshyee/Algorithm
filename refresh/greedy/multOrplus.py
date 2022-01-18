"""
문제: 각 자리가 숫자(0-9)로 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 하나씩 모든 숫자를 확인 하며, 숫자 사이에
'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램
(단, 모든 연산은 왼쪽부터 순서대로 이루어짐)

조건: 입력의 가장 큰 수는 항상 20억 이하의 정수가 되도록

! 정당성 부여하기
-> 0(다른 수가 곱해졌을 때 0으로 만듬) 혹은 1(더하는게 곱하는것 보다 커짐) 을 제외할 시, 모두 곱할때 값이 훨씬 커짐!
-> 문자열의 시작이 0 이라면, 다음 인덱스의 값이 0이 아니더라도 최종값이 0이 될 수 있으므로 꼭 확인해주기

! 자료의 type
int형은 21억 자리수 정수까지 커버 가능!
"""

s = input()
sum = int(s[0]) # 첫 자리 먼저 더해주기
for i in range(1,len(s)): # 0번쨰 index는 먼저 추가했으므로, 1번째 index 부터
    i = int(i)
    if i <= 1 or sum <= 1: # i가 0 혹은 1일때, sum이 0 혹은 1일때
        sum += i # 덧셈연산 수행
    else:
        sum *= i
print(sum)
