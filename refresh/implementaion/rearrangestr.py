string = input()
s = 0
new = []

for i in string:
    if i >= '1' and i <= '9':
        s += int(i)
    else:
        new.append(i)
new.sort()
print(''.join(new) + str(s))
