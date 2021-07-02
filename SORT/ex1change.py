'''
두 배열 원소 교체
a,b 배열(원소: n개, 모두 자연수)
최대 K번의 바꾸기 연산 가능(두 배열의 원소 하나를 서로 교체하는 연산)
배열 A의 원소합이 최대가 되도록
입력: N,K,배열 A,배열 B
출력: A배열 원소의 최대 합
'''
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort() #배열 B내림차순으로 정렬하면 연산이 더 편함
#b.sort(reverse = True)

for i in range(k):
	if a[i] < b[len(b)-i-1]:
		a[i] = b[len(b)-i-1] # 원래 원소 보장하기 -> 스왑으로
		#a[i],b[i] = b[i],a[i] > b를 내림차순으로 정렬했을 경우
		#a[i],b[len(b)-i-1] = b[len(b)-i-1],a[i] > 현싱태에서 원래 원소 보장할 경우

print(a)
print(sum(a))
