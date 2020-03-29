def myfunc(a, b, c, d):
    return min(a, min(b, min(c, d)))


arr = [int(i) for i in input().split()]
print(myfunc(arr[0], arr[1], arr[2], arr[3]))