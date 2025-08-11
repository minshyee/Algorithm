a, b, c = map(int, input().split())

# Please write your code here.
res = a * b * c

def f(n):
    if n == 0:
        return 0
    r = n % 10
    return r + f(n//10)

print(f(res))