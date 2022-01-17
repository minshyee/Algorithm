def left(visited,left_ind):
	left = 0
	while visited[left_ind] != 1:
		left += 1
		left_ind -= 1
		print('L',[left,left_ind])
	return [left,left_ind]

def right(visited, right_ind):
	right = 0
	while visited[right_ind] != 1:
		right += 1
		right_ind += 1
		print('R',[right, right_ind])
	return [right, right_ind]


def solution(name):
	ind = 0
	cnt = 0
	visited = []

	l = len(name)
	if 'A' not in name:
		cnt += l-1
		# print('cnt1',cnt)
	else:
		for x in name:
			if x == 'A':
				visited.append(0)
			else:
				visited.append(1)

		visited[0] = 0

		while max(visited) != 0:
			l_val = left(visited,ind)
			r_val = right(visited,ind)

			if l_val[0] < r_val[0]:
				cnt += l_val[0]
				visited[l_val[1]] = 0
				ind = l_val[1]
				# print('cnt2',cnt)
			else:
				cnt+= r_val[0]
				visited[r_val[1]] = 0
				ind = r_val[1]
				# print('cnt3',cnt)

	for i in range(l):
		n = ord(name[i])
		if n < 78:
			cnt += n - 65
			# print('cnt4',cnt)
		else:
			cnt += 91 - n
			# print('cnt5',cnt)
	return cnt

print(solution("ABAAAAAAAAABB"))
