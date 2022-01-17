'''
2차원 공간이 나오는 문제
8*8 - 공간 나갈 수 없음
나이트 - 수평 2칸 수직 1칸 or 수평 1칸 수직 2칸
나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 위치 표현
행 1~8 / 열 a~h
'''

now = input()

x, y = int(now[1]), 0

dx = [1,2,1,2,-1,-2,-1,-2]
dy = [2,1,-2,-1,2,1,-2,-1]

cnt = 0

coulmns = ['a','b','c','d','e','f','g','h']
for i in range(len(coulmns)):
	if now[0] == coulmns[i]:
		y = (i + 1)

for j in range(len(dx)):
	nx = x + dx[j]
	ny = y + dy[j]
	if nx < 1 or nx > 8 or ny < 1 or ny > 8:
			continue
	else:
		cnt += 1

print(cnt)
