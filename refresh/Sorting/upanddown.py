
n = int(input())
num_lst = []

for i in range(n):
    num_lst.append(int(input()))

# 퀵정렬로 구현
def quick_sort(lst):
    l = len(lst)
    if l <= 1:
        return lst

    pivot = lst[0]
    # 큰 쪽
    left = [lst[j] for j in range(1,l) if lst[j] > pivot ]
    # 작은 쪽
    right = [lst[k] for k in range(l-1,1,-1) if lst[k] < pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

ans = quick_sort(num_lst)
for i in ans:
    print(i, end=' ')

##==================================================================================

# ㅋ..
# 그냥 기본 라이브러리 사용하기...

num_lst = sorted(num_lst, reverse=True)
