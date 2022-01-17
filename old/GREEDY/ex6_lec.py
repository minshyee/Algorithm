'''
완전 탐색 24*60*60 = 86400 뿐 -> 충분히 빨리 가능
python 1초 2천만번
'''

n = int(input())

cnt = 0
for i in range(n+1): #시
	for j in range(60): #분
		for k in range(60): #초
			# 매 시각 안에 '3'이 포함되어 있는지 체크
			if '3' in str(i) + str(j) + str(k):
				cnt += 1

print(cnt)
