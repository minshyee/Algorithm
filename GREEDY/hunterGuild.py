n = input('모험가의 총 수 :')
fears = list(map(int, input('공포도 :').split()))

# if len(fear) != n:
# 	print('너무 많은 공포도가 입력 되었습니다.')
# else:

fears.sort()
g_count = 0 #그룹수
g_tmp = 0 #그룹에 들어갈 모험가 수

for fear in fears: #공포도를 돌면서
	g_tmp += 1 #모험가 1명 존재
	if g_tmp >= fear: #모험가수가 공포도보다 크거나 같으면
		g_count +=1 #그룹 수 를 증가 시킨다
		g_tmp = 0 #새로운 그룹만들기를 위한 초기화

print(g_count)

# while len(fears)<1:
# 	g = [fears[0]]
# 	for i in range(1,len(fears)):
# 		if len(g) < g[0]:
# 			if fears[i] < g[0]:
# 				g.append(fears[i])
# 				fears.remove(i)
# 		else:
# 			print(g)
# 			g_count +=1
# print(g_count)
