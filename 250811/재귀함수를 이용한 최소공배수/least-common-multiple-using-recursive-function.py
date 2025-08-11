n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    while(b != 0):
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b // gcd(a, b) if a and b else 0

first = arr[0]
for i in arr[1:]:
    first = lcm(first, i)

print(first)
