n = int(input())
plan = input().split()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

x, y = 1, 1
for i in plan:
    p_x, p_y = x, y
    if i == 'L':
        x += dx[0]
        y += dy[0]
    elif i == 'R':
        x += dx[1]
        y += dy[1]
    elif i == 'U':
        x += dx[2]
        y += dy[2]
    else:
        x += dx[3]
        y += dy[3]
    if x < 1 or x > n or y < 1 or y > n:
        x, y =p_x, p_y


print(x,y)


# -------------------------------------------------------
# -------------------------------------------------------




n = int(input())
plan = input().split()

set_p = ['L','R','U','D']
dx = [-1,1,0,0]
dy = [0,0,-1,1]

x, y = 1, 1

for i in plan:
    for j in range(4):
        if i == set_p[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x,y)
