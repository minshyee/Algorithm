s = input()

cur = s[0]
flip_cnt = 0

for i in s[1:]:
  if cur != i:
    flip_cnt += 1
    cur = i

if flip_cnt % 2 == 0:
  print(flip_cnt//2)
else:
  print((flip_cnt+1)//2)

#------------------------------------------------
#------------------------------------------------



data = input()
count0 = 0
count1 = 0

if data[0] == '1':
  count0 += 1
else:
  count1 += 1

for i in range(len(data)-1):
  if data[i] != data[i+1]:
    if data[i+1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count0,count1))
