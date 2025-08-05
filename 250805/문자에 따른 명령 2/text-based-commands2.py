dirs = input()

# Please write your code here.
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


d, nx, ny = 0, 0, 0

for c in dirs:
    if(c == 'L'):
        d -= 1
        d %= 4
    elif(c == 'R'):
        d += 1
        d %= 4
    elif(c == 'F'):
        nx += dx[d]
        ny += dy[d]

print(nx, ny)