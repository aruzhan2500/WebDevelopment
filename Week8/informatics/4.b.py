n = int(input())
a = [int(i) for i in input().split()]
print(*[i for i in a if not i % 2])
