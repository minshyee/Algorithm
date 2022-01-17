n = int(input())
people=[]
for i in range(n):
	name, age =  input().split()
	people.append((name, age))

people.sort()
#people = sorted(people, key= lambda student: student[1])

#i가 student
for i in people:
	print(i[0], end=" ")
