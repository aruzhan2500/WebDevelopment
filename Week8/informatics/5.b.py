def pow(a, n):
    if n == 0:
        return 1
    return a * pow(a, n - 1)


arr = [int(i) for i in input().split()]
print(pow(arr[0], arr[1]))