N = int(input())

# Please write your code here.
def f(n):
    if n < 10:
        return pow(n, 2)

    return f(n//10) + pow((n%10),2)

print(f(N))