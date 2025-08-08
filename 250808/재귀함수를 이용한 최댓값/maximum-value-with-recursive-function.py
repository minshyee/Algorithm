n = int(input())
arr = list(map(int, input().split()))

n -= 1
# Please write your code here.
def f(n, maxNum):
    if n == -1:
        return maxNum
    
    if(arr[n] > maxNum):
        return f(n-1, arr[n])
    else:
        return f(n-1, maxNum)

print(f(n, 1))