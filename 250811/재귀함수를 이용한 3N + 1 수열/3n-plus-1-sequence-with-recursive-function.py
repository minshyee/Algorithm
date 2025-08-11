n = int(input())

# Please write your code here.

def f(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + f(n/2)
    if n % 2 == 1:
        return 1 + f(n*3 + 1)

print(f(n))