num = input()

n =[]
for i in num:
	n.append(int(i))
print(n)

if n[0] < 2:
	s = n[0] + n[1]
	k = 2
else:
	s = n[0]
	k = 1

for j in range(k,len(n)):
	if n[j] < 2:
		s += n[j]
	else:
		s *= n[j]

print(s)

#better
# s=0
# for j in num:
# 	j = int(j)
# 	if j >= 2  and s > 1:
# 		s *= j
# 	else:
# 		s+= j

# print(s)
