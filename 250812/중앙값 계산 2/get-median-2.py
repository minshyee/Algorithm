n = int(input())
arr = list(map(int, input().split()))

res = []
# Please write your code here.
def cen(arr):
    arr.sort()
    s = len(arr)
    return arr[s//2]

for i in range(n):
    res.append(arr[i])
    if i%2 == 0:
        print(cen(res), end = " ")


    