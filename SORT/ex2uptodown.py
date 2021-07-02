n= int(input())

numbers = []

for i in range(n):
	numbers.append(int(input()))

numbers.sort(reverse = True) #method 사용
#numbers = sorted(numbers, reverse = True) #라이브러리 사용

for j in numbers:
	print(j,end=" ")
