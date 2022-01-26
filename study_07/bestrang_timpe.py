n_list = []
def list_prime(n):
	# res = n
	# print(n)
	test = [1] * (2*n +1)
	test[0] = 0
	test[1] = 0
	for i in range(2, 2*n + 1):
		for j in range(2, int(round(i**0.5, 0))+1): # 제곱근을 기준으로 약수는 대칭을 이루기 떄문에
			if i % j == 0:
				# print(i,'not')
				test[i] = 0
				# res -= 1
				break
	# print(test, len(test))
	return test

while True:
    n = int(input())
    if n == 0:
        break
    else:
        n_list.append(n)

p_list = list_prime(max(n_list)) # 매번 검사할 필요는 없다! : key
# cnt=[0] * len(n_list)
# for i in range(len(n_list)):
for n in n_list:
    print(p_list[n+1:2*n+1].count(1)) # index가 값으로

