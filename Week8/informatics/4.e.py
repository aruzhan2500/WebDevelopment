n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for j in range(0, n - 1):
    if (a[j] > 0 and a[j + 1] > 0) or (a[j] < 0 and a[j + 1] < 0):
        ans = 1
        break
if ans == 1:
    print('YES')
elif ans == 0:
    print('NO')