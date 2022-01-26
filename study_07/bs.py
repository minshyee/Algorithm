n = int(input())
info = sorted(list(map(int, input().split())))
m = int(input())
s_lst = list(map(int, input().split()))

def searching(lst, num, med):
    if med < 1:
        return 0
    else:
      if lst[med] == num:
          return 1
      elif lst[med] < num:
          return searching(lst[med+1:], num, len(lst[med+1:])//2)
      else:
          return searching(lst[:med], num, med//2)

for i in s_lst:
    print(searching(info, i, n//2))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

n = int(input())
info = set(map(int, input().split()))
m = int(input())
s_lst = list(map(int, input().split()))

for i in s_lst:
    print(1) if n in info else print(0)
