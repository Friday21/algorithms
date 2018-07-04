"""
教材187页， 三向切分快速排序
"""


def three_way_sort(a, lo, hi):
    if hi <= lo:
        return
    lt = lo
    gt = hi
    cmp = a[lo]
    i = lo
    while i <= gt:
        if a[i] == cmp:
            i += 1
        elif a[i] > cmp:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
    three_way_sort(a, lo, lt-1)
    three_way_sort(a, gt+1, hi)


if __name__ == '__main__':
    raw_array = [1, 3, 3, 2, 2, 2, 7, 6, 6, 9, 4]
    three_way_sort(raw_array, 0, len(raw_array)-1)
    print(raw_array)
