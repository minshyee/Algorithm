s = input()

ind=0
corpus=[]
c = 0

for i in range(1,len(s)):
	if s[ind] != s[i]:
		if s[ind] == '0':
			c += 1
		corpus.append(s[ind:i])
		ind = i
corpus.append(s[ind:])

if c < (len(corpus)/2):
	print(c)
else:
	print(len(corpus)-c)
