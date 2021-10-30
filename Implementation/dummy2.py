n = int(input()) # size of board
k = int(input()) # number of apple

board = [[0]*n for i in range(n)]

turn = [] #snake turn info

for q in range(k):
	place = list(map(int, input().split()))
	board[place[0]-1][place[1]-1] = 1

l = int(input())
for i in range(l):
	t = list(input().split())
	t[0] = int(t[0])
	turn.append(t)

time = 0
d_ind = 0
snake =[[0,0]]
col = 0 #x
row = 0 #y
dc = [0,1,0,-1]
dr = [1,0,-1,0]

board[row][col] = 2


while True:
	if turn and turn[0][0] == time:
		# print('t',time)
		if turn[0][1] == 'D':
			d_ind = (d_ind + 1) % 4
		else:
			d_ind = (d_ind - 1) % 4
		# print('d',d_ind)
		turn.remove(turn[0])

	# print('(c,r)',col, row)
	# print('d',d_ind)
	x = col + dc[d_ind]
	y = row + dr[d_ind]
	# print('x',x,'y',y)
	if x > n-1 or y > n-1 or x < 0 or y < 0:
		time += 1
		break
	snake.append([x,y])
	if board[x][y] == 1:
		# print('1일때\n')
		board[x][y] = 2
	elif board[x][y] == 2:
		# print('2일때\n')
		time += 1
		break
	else:
		board[x][y] = 2
		tail = snake.pop(0)
		board[tail[0]][tail[1]] = 0
		# board[x - (dc[d_ind]*s_len)][y - (dr[d_ind]*s_len)] = 0 이건 한줄으로만 접근이 가능 꺽인경우 제어필요

		# print('0일때\n')
	col = x
	row = y
	time += 1

	# print('------------------\n')
	# for i in board :
	# 	for j in i:
	# 		print(j,end=" ")
	# 	print()
	# print('------------------\n')

# for i in board :
# 		for j in i:
# 			print(j,end=" ")
# 		print()
print(time)
