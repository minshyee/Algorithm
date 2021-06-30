#0,1제외 모두 곱셈으로 넣는게 이득
num = [int(i) for i in input()]

sum = num[0]
'''
sum = 0
for i in num:
	if sum == 0:
		sum += i
'''
for i in num:
	if i <= 1 or sum <=1:  # if i == 0 or i == 1:
		sum += i
	else:
		sum *= i
print(sum)
# 코드를 줄일 수 있음!
