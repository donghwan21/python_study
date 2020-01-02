def sqare_root(n):
    s = 0
    for i in range(1, n+1):
        s = i**2+s
    return s


print(sqare_root(10))
# 시간 복잡도:O(n)
