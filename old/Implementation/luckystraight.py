score = input()
left = 0
right = len(score) - 1
lval = 0
rval = 0

if right % 2 == 0:
	print('READY')
else:
	while left < right:
		lval += int(score[left])
		rval += int(score[right])
		left += 1
		right -= 1
	if lval == rval:
		print('LUCKY')
	else:
		print('READY')
