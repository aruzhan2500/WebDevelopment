n = int(input())
a = [int(i) for i in input().split()]
s = 0
for j in range(1, n - 1):
    if (a[j] > a[j - 1]) & (a[j] > a[j + 1]):
        s += 1
print(s)