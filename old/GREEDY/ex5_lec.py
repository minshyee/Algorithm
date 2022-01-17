'''
일련의 명령에 따라 개체를 차례대로 이동 : 시뮬레이션 유형 -> 구현중요
시뮬레이션 = 구현 = 완전탐색 비슷
'''
n = int(input())
x,y =1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for plan in plans:
	for i in range(len(move_type)):
		if plan == move_type[i]:
			result_x = x + dx[i]
			result_y = y + dy[i]

	#움직일 죄표가 공간 안에 있는지 확인
	if result_x < 1 or result_x > n or result_y < 1 or result_y > n:
		continue
	#실제로 이동
	x,y = result_x, result_y

print(x,y)
