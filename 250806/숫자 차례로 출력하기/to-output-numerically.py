n = int(input())

# Please write your code here.
def print_num(n):
    if n == 0:
        return
    
    print_num(n-1)
    print(n, end=" ")

def print_nums(n):
    if n == 0:
        return
    
    print(n, end=" ")
    print_nums(n-1)


print_num(n)
print()
print_nums(n)