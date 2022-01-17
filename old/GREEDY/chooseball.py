n,m = map(int,input().split())
ball = list(map(int,input().split()))

i = 0
chosen = []
while i != len(ball):
	for j in range(i+1,len(ball)):
		if ball[i] != ball[j]:
			chosen.append((ball[i], ball[j]))
	i += 1
print(len(chosen))
