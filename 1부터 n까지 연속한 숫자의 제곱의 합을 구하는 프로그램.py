import math


def square_root(n):
    s = 0
    for i in range(1, n+1):
        s = i**2+s
    return s


def square_root2(n):
    s = 0
    s = n*(n+1)*(2*n+1)/6
    return s


print('O(n)'+str(square_root(10)))
print('O(1):'+str(square_root2(10)))
# 시간 복잡도:O(n)
