def sum_n(n):  # 노가다 계산 복잡도 (빅오 표기법):O(n)
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(sum_n(10))
print(sum_n(100))


def sum_a(n):  # 가우스 계산 복잡도(빅오 표기법):O(1)

    s = 0
    s = n(n+1)/2
    return s


print('s='+str(sum_n(20)))
