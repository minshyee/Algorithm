n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def sortArr(n):
    return sorted(n)

def reverseArr(n):
    return n.sort(reverse=True)

def printStr(arr):
    return " ".join(map(str, arr))

print(printStr(sortArr(nums)))
print(printStr(reverseArr(nums)))