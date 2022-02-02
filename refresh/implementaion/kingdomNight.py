cur = input()

x = ord(cur[0]) - 97
y = int(cur[1])-1

# 방향벡터
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

if nx < 8 and nx > -1 and ny < 8 and ny > -1: # 체스판 '안'인지 확인 (index 0부터 시작)
        cnt += 1
print(cnt)
