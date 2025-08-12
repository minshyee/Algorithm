n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
res = "Yes"
for i in A:
    if i not in B:
        res = "No"
        break
print(res)