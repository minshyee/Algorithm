n_list = []

def count_prime(n):
	# res = n

	test = list(range(n+1,2*n+1))
	for i in range(n+1, 2*n + 1):
		for j in range(2, int(round(i**0.5, 0))+1):
			if i % j == 0:
				# print(i,'not')
				test.remove(i)
				# res -= 1
				break
	print(test, len(test))
	return test

# 입력
while True:
    n = int(input())
    if n == 0:
        break
    else:
        n_list.append(n)

sorted(n_list)
p_list = count_prime(n_list.pop)
for n in n_list:
    print(count_prime(n))
