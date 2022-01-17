string = input()
s = 0
for i in string:
	if i >= '0' and i <= '9':
		s += int(i)
		string = string.replace(i,"")
string = ''.join(sorted(string))
print(string + str(s))
