N = int(input())

# Please write your code here.
def f(n):
    if n % 2 == 0:
        return fEven(n)
    elif n % 2 == 1:
        return fOdd(n)
        
def fOdd(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return fOdd(n-1)
    elif n % 2 == 1:
        return n + fOdd(n - 1)

def fEven(n):
    if n == 2:
        return 2
    
    if n % 2 == 0:
        return n + fEven(n-1)
    elif n % 2 == 1:
        return fEven(n-1)

print(f(N))