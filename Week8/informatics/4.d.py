n = int(input())
a = [int(i) for i in input().split()]
k = 0
for j in range(1, n):
    if a[j] > a[j - 1]:
        k += 1
print(k)