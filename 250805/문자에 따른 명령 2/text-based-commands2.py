dirs = input()

# Please write your code here.
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

dir = 0
nx, ny = 0, 0

coord = 's'

for c in dirs:
    if(c == 'L'):
        dir = (dir + 1) % 4
    elif(c == 'R'):
        dir = (dir -1 + 4) % 4
    elif(c == 'F'):
        nx += dx[dir]
        ny += dy[dir]

print(nx, ny)
        

