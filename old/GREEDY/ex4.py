#모험기 길드 5:54-6:20(25)
'''
공포도 x , x명이 같이가야 / 최대 모험가 길드수

입력: 모험가 수, 모험가 별 공포도
모험가 길드원 수 : 공포도 최대값 기준
길드에 안들어가도 상관X

정당성???????

'''
n = int(input())
fear = [int(i) for i in input().split()]

cnt = 0
result = 0

while True:
	fearest = max(fear)
	for x in fear:
		if x <= fearest and cnt < fearest:
			fear.remove(x)
			cnt += 1
		else:
			cnt = 0
			result += 1
	if fear == []:
		result += 1
		break

print(result)
