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
		if turn[0][1] == 'D':
			d_ind = (d_ind + 1) % 4
		else:
			d_ind = (d_ind - 1) % 4

		turn.remove(turn[0])

	x = col + dc[d_ind]
	y = row + dr[d_ind]
	if x > n-1 or y > n-1 or x < 0 or y < 0:
		time += 1
		break
	snake.append([x,y])
	if board[x][y] == 1:
		board[x][y] = 2
	elif board[x][y] == 2:
		time += 1
		break
	else:
		board[x][y] = 2
		tail = snake.pop(0)
		board[tail[0]][tail[1]] = 0

	col = x
	row = y
	time += 1

print(time)
