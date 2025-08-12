n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
arr = [i for i in str if i.startswith(t)]
arr.sort()
print(arr[k-1])