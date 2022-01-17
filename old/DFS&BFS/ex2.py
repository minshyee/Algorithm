'''
n: 얼음틀의 세로
m: 얼음틀의 가로
얼음 틀 형태 주어짐
구멍 0 틀 1
한번에 만들 수 있는 아이스크림 개수
'''
n, m = map(int, input().split())

icecase = []
graph = []
visited = [False] * m

for i in range(n):
	icecase.append([int(v) for v in input()])
"""
for j in range(n):
	graph.append([])
	for k in range(m):
		if icecase[j][k] == 0:
			graph[j].append(k)

print(graph)
 """
def dfs(graph, v, visited):
	visited[v]=True
	print(v,end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph,i,visited)




