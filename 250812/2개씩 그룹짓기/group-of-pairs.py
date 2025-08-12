n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

arr = []
while(nums):
    arr.append(nums[0] + nums[-1])
    nums.pop(0)
    nums.pop(-1)

print(max(arr))