'''
00:00:00 - N:59:59 > 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

시 - 3/13/23
분 - 3/13/23/30~39/43/53 : 15
초 - 3/13/23/30~39/43/53 : 15

15 * n -> 분
59-15 =44 /44 * 15 * n -> 초
'''
n = int(input())

hours = [3,13,23]
result = 0
cnt = 0

for hour in hours:
	if n >= hour:
		result += (60*60)
		cnt += 1

min = 60*15*n
sec = 45*15*n
result += (min + sec)

print(result)
