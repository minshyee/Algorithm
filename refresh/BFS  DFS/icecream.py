n, m = map(int, input().split())
icemap = [input() for i in range(n)]
icemap = [[int(i[j]) for j in range(m)] for i in icemap]
# visit = [True  if i[j] == 1 else False for i in icemap for j in range(m)]

def search(map, x, y):
  dx = [1,-1, 0, 0]
  dy = [0, 0, 1, -1]
  if x >= n or x < 0 or y < 0 or y >= m: # index 확인
    return False
  if map[x][y] == 0:
    map[x][y] = 1
    for i in range(4): #동서남북 접근
      search(map, x+dx[i], y+dy[i])
    return True
  return False

cnt = 0
# 모든 map 탐색
for i in range(n):
  for j in range(m):
    if search(icemap, i, j):
      cnt += 1
print(cnt)
