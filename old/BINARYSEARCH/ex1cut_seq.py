'''
input: 떡의 개수 n, 손님의 요청 길이 m
output: 최대 높이 h
절단된 길이의 합을 손님이 가져감
'''
n,m = map(int,input().split())
ricecake = list(map(int,input().split()))
print(ricecake)
"""
# 완전 잘못 생각한 부분
# ricecake.sort()

# mid =  n//2
# center = ricecake[mid]
while m != sum:
	if m!=sum:
		center -= 1
		sum = 0
	for i in ricecake:
		if i - center > 0:
			sum += (i-center)

print(center) """
'''Sol
조건의 만족 여부에 따라 탐색범위를 좁혀 해결할수 있음
탐색범위가 클때 이진 탐색을 떠올릴것!
'''
mid = (max(ricecake) // 2) +1
sum = 0

while sum != m:
	if sum > m:
		mid+= 1
		sum = 0
	else:
		mid -= 1
		sum = 0
	print("mid",mid)
	for i in ricecake:
		if i - mid > 0:
			sum += (i - mid)
			print("sum",sum)

print(mid)
