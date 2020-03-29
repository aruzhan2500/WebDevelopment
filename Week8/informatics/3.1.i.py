a = int(input())
cnt = 0
for x in range(1, a+1):
    if(a % x == 0):
        cnt += 1
print(cnt)