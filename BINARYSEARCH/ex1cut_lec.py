n,m = map(int,input().split())
ricecake = list(map(int,input().split()))

#이진 탐색을 위해 시작점, 끝점 설정
start = 0
end = max(ricecake)

#이진탐색 수행
result = 0
while(start <= end):
	total = 0
	mid = (start + end) // 2

	#떡의 양 계산
	for x in ricecake:
		if x>mid:
			total += x - mid

	#양 부족할때
	if total < m:
		end = mid -1

	#양이 많을 때 > 덜 자르기
	else:
		result = mid #최대한 덜 자를때가 정답
		start = mid + 1

print(result)
