N = int(input())

# Please write your code here.
def print_N(n):
    if n == 0:
        return
    
    print(n, end=' ')
    print_N(n-1)
    print(n, end=' ')

print_N(N)