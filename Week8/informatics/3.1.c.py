from math import sqrt

a = int(input())
b = int(input())
for x in range(a, b+1):
    for y in range(1, int(sqrt(x))+1):
        if(y * y == x):
            print(x, end = " ")