'''
오름차순 정렬 -> 최소한의 모험가의 수만 포함하여 그룹결성
=> 최대한 많은 길드를 만들어야 == 길드 안에 사람이 적고 길드가 많아야
즉, 내림차순이 아니라 오름 차순으로 풀어야

list.sort() : 기본설정이 오름차순(작 -> 큰) 정렬
'''

n = input()
fear = [int(i) for i in input().split()]
fear.sort()

cnt = 0#현재 그룹에 포함된 모험가의 수
result = 0 #총 그룹의 수

for x in fear: #공포도를 낮은 것 부터 하나씩 확인
	cnt += 1 #현재 그룹에 해당 모험가 ㅠㅗ함
	if cnt >= x: #현재 그룹에 포함되 모험가 수 가 현재 공포도 이상이라면 그룹 결성
		result += 1 #총 그룹의 수 증가시키기
		cnt = 0 #현재 그룹에 포함된 모험가 수 초기화
	'''
	if cnt <= x:
		cnt +=1
	else:
		if cnt > x:
			result += 1
			cnt = 0
			'''

print(result)

