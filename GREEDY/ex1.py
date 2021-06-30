change = int(input("거스름돈 : "))
coin = [500,100,50,10]
cnt =0

for i in coin:
	cnt += change // i
	change = change % i

print(f"최소 동전의 개수는 {cnt}개 입니다")
