n = int(input())
cnt = 0

checker = sum([1 if '3' in str(j) else 0 for j in range(60)])

for i in range(n+1):
    if i == 3 or i == 13 or i == 23:
        cnt += 3600
    else:
        cnt += (45*checker) + (checker * 60)
print(cnt)

##---------------------------------------------
# 강의 답안
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 cnt += 1
