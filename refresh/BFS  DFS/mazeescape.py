n, m = map(int, input().split())
maze = [[int(i[j])for j in range(m)] for i in [input() for _ in range(n)]]

'''
def dfs(x,y,cnt,res=[]):
    if x<0 or y<0 or x >= n or y >=m:
        return False
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if maze[x][y] == 1:
        cnt += 1
        print('f',x,y)
        print(cnt)
        res.append(cnt)
        maze[x][y] = 0
        for i in range(4):
            dfs(x+dx[i],y+dy[i],cnt,res)
        if x == n-1 and y == m-1:
            return cnt

    return False

# cnt = 0
# for i in range(n):
#     for j in range(m):
#         now, cnt = dfs(j,i,cnt)
#         if now:
#             print('------------')
#             print(i,j)
#             print(cnt)
# print(cnt)
# print(maze)
cnt = 0
res = dfs(0,0,cnt)
if res:
    print(1)
    print(res)
print(maze)

'''

from collections import deque


queue = deque()
visited = [[False if i[j] == 1 else True for j in range(m)] for i in maze]

cnt = 1
dr = [0,1,-1,0]
dc = [1,0,0,-1]

# 시작 위치 방문 및 큐 삽입
queue.append((0,0))
visited[0][0] = True

# bfs 시작
while queue:
    cur = queue.popleft()
    r, c = cur[0], cur[1]


    for i in range(len(dr)):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if maze[nr][nc] == 1 and not visited[nr][nc]: # 1이거나 미방문이면
            queue.append((nr,nc))
            visited[nr][nc] = True
            cnt += 1
            print("이프문 들어간다 후",nr,nc, '->', cnt)

            if nr == n-1 and nc == m-1: # 도착지에 도착하면 멈춤
                break
    if nr == n-1 and nc == m-1:
        break

    print("리얼현재",nr,nc, '->', cnt)

print(cnt)
