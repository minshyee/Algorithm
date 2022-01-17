'''
N*N 정사각형 - 가장 왼쪽 위 좌표:(1,1) / 가장 오른쪽 아래 좌표:(N,N)
여행자 상,하,좌,우 이동 가능 / 시작은 항상 (1,1)
L:왼 한칸 R: 오 한칸 U: 위 한칸 D: 아래 한칸
공간을 벗어나는 움직임은 무시된다
'''
n = int(input())
plan = [i for i in input().split()] #input().split()와 같은 결과

x,y =1,1

for j in plan:
	if j == 'L':
		y -= 1
		if y <= 0:
			y+=1
	elif j == 'R':
		y += 1
		if y > n:
			y-=1
	elif j == 'U':
		x -= 1
		if x <= 0:
			x+=1
	elif j == 'D':
		x += 1
		if x > n:
			x-=1
	else:
		x = 1
		y = 1

print(x,y)
