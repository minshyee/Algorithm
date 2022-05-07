#Tabulation

n = int(input())

res =[0]*(n+1)
for i in range(2,n+1):
    res[i] = res[i-1]+1
    if i % 5 == 0:
        case1 = res[i//5]+1
        res[i] = min(res[i], case1)
    if i % 3 == 0:
        case2 = res[i//3]+1
        res[i] = min(res[i], case2)
    if i % 2 == 0:
        case3 = res[i//2]+1
        res[i] = min(res[i], case3)
print(res[n])



#memoiozation
