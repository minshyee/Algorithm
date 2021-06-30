'''
n*m 미로
시작위치(1,1) 한번에 한칸
괴물 O : 0 , 괴물 X : 1
탈출하기 위한 최소 칸수(시작, 끝칸 모두 포함)
'''


n,m = map(int, input().split())

graph=[]


for i in range(n):
	graph.append(list(map(int, input())))

