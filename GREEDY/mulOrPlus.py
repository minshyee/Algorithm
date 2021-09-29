num = input()

n =[]
for i in num:
	n.append(int(i))
print(n)

s=0
tmp=1
for j in n:
	if j == 0 or j == 1:
		s += j
	else:
		tmp *= j

s += tmp
print(s)
