from tarfile import LENGTH_LINK


n = int(input())
product = set(map(int, input().split()))

m = int(input())
user = list(map(int, input().split()))

for i in range(m):
    pivot = user[i]
    if pivot in product:
        print('yes', end= " ")
    else:
        print('no', end=' ')
