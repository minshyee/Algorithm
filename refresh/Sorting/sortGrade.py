from ast import operator


n = int(input())
lst = {}
for i in range(n):
    info = input().split()
    lst[info[0]] = int(info[1])

sort = sorted(lst.items(),key=lambda x: x[1])

for key, value in sort:
    print(key)
