n,m = map(int, input().split())
x, y, d_ind = map(int,input().split())
map = []

dir = [(0,-1), (1,0), (0,1), (-1,0)]


# map 입력받기
for i in range(n):
    row = input().split()
    map.append(row)

cnt = 0
t_cnt = 0

def turn_left(d, count):
    d -= 1
    count += 1
    if d == -1:
        d = 3
    return d, count

map[x][y] = 1

while x<n and x > -1 and y<m and y > -1:

    # 왼쪽으로돌기
    d_ind, t_cnt = turn_left(d_ind, t_cnt)
    print('ind/cnt ',d_ind, t_cnt)
    # 새로운 곳의 좌표
    nx = x + dir[d_ind][0]
    ny = y + dir[d_ind][1]
    print('n x:',nx,'y',ny)

    if map[nx][ny] == 0:
        x, y = nx, ny
        map[x][y] = 1
        cnt += 1
        t_cnt = 0
        print('map', map)
    else:
        d_ind, t_cnt = turn_left(d_ind, t_cnt)
        print('ind/cnt2 ',d_ind, t_cnt)

    if t_cnt == 4:
        nx = x - dir[d_ind][0]
        ny = y - dir[d_ind][1]
        if map[nx][ny] == 0:
            x, y = nx, ny
            map[x][y] = 1
            cnt += 1
            t_cnt = 0
        else:
            break
        t_cnt = 0
print(cnt)
