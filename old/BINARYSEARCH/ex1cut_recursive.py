n,m = map(int,input().split())
ricecake = list(map(int,input().split()))

def bsearch(list, min, max):
	mid = (min+max) // 2
	print("mid",mid)
	sum = 0
	for i in list:
		if i - mid >0:
			sum += (i-mid)
			print("sum",sum)
	if sum == m:
		return mid
	if sum > m:
		return bsearch(list, mid+1, max)
	elif sum < m:
		return bsearch(list, min, mid-1)


result = bsearch(ricecake,0,max(ricecake))
print(result)
