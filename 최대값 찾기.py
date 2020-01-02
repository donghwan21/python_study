def find_max(a):  # 최대값 찾기
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
        return max_v


def find_max_idx(a):  # 최대값 위치 찾기
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


v = [17, 98, 18, 33, 58, 7, 33, 42]
print(find_max(v))
print(find_max_idx(v))
