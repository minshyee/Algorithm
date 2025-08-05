n = int(input())

# Please write your code here.
def print_N(n):
    if n == 0:
        return
    print_N(n-1)
    print(n, end=' ')

def print_N_rev(n):
    if n == 0:
        return
    print(n, end=' ')
    print_N_rev(n-1)

print_N(n)
print()
print_N_rev(n)