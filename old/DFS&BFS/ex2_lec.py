'''
1. 특정 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서
	아직 방문하지 않은 지점이 있다면 해당 지점을 방문
2. 방문한 지점에서 다시  상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복
	연결된 모든 지점을 방문할 수 있음
3. 모든 노드에 대해 과정 반복, 방문하지 않은 지점 수 카운트
'''


#특정 노드를 방문 > 연결된 모든 노드 방문
def dfs(x,y):
	#주어진 범위가 벗어나면 종료
	if x<=-1 or x >= n or y <= -1 or y>=m:
		return False

	#현재 노드 방문 여부 체크
	if graph[x][y] == 0:
		graph[x][y] = 1 #방문처리

		#현재 노드에서 연결된 상하좌우 노드 재귀 호출을 통해 방문
		dfs(x-1, y)
		dfs(x,y-1)
		dfs(x+1,y)
		dfs(x,y+1)

		return True
	return False

n,m =  map(int, input().split())

graph = []
for i in range(n):
	#graph.append([int(l) for l in input()])
	graph.append(list(map(int, input())))
result = 0

#모든 좌표를 돌며 음료수 넣기
for j in range(n):
	for k in range(m):
		#현재 위치에서 dfs수행
		if dfs(j,k) == True:
			result += 1

print(result)
