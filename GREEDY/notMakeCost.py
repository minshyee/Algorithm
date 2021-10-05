n = int(input())
coin = list(map(int, input().split()))

coin.sort()
target = 1

for c in coin: #화폐단위를 돌면서
	if target < c: # target값이 단위값보다 작으면
		break
	else:
		target += c
print(target)

'''
n = int(input())
coin = list(map(int,input().split()))

coin.sort()
l = len(coin)
n = 1

if coin[0] != n:
	print(n)
else:
	n += 1
chosen = []
i = 0

while i != l-1:
	print('i',i)
	# print(j)
	for j in range(1,len(coin)-i):
		chosen.append((coin[i],coin[i+j]))
		print(chosen)
	i += 1

num = []
for k in range(len(chosen)):
	num.append(chosen[k][0]+chosen[k][1])

num = list(set(num))
num.append(coin[0])
print(num)
'''
