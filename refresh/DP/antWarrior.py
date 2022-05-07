n = int(input())

warehouse = list(map(int, input().split()))

# 최소한 1칸 이상 떨어진 창고여야
res = [0]*n

for i in range(n):
