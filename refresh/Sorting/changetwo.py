
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))


for i in range(k):
    al = len(a)-1
    if a[i] < b[al-i]:
        a[i], b[al-i] = b[al-i],a[i]
    else:
        break

print(sum(a))


#==========================================================================
#==========================================================================

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i], a[i]
    else:
        break
print(sum(a))
