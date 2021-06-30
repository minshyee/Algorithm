#현재 나이트 위치 입력받기

now = input()

x = int(now[1])
y = int(ord(now[0])) - int(ord('a')) + 1 # 아스키 코드사용
'''
ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.
※ ord 함수는 chr 함수와 반대이다.
'''

steps = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]

cnt = 0
for step in steps:
	nx = x + step[0]
	ny = y + step[1]
	#이동 가능하면 카운트 증가
	if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
		cnt += 1

print(cnt)
