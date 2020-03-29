n = int(input())
a = [int(i) for i in input().split()]
for j in range(0, n // 2):
    c = a[j]
    a[j] = a[n - j - 1]
    a[n - j - 1] = c
for j in range(0, n):
    print(a[j], end=' ')