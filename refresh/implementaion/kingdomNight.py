cur = input()

x = ord(cur[0]) - 97
y = int(cur[1])-1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
cnt = 0

print(x,y)
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx,ny)
    if nx < 8 and nx > -1 and ny < 8 and ny > -1:
        cnt += 1
print(cnt)
