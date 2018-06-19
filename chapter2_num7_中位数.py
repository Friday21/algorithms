"""
教材 221页， 找出一组元素中的中位数

思路：
使用快速排序的切分方法，则a[lo..j-1] 小于等于 a[j], a[j+1..hi] 大于等于a[j]
如果 j = N/2, 则返回a[j],
如果 j < N/2, 则继续切分a[j+1..hi]
如果 j > N/2， 则继续切分a[lo..j-1]
"""


def find_middle(a):
    N = len(a)
    low = 0
    high = N - 1
    while low < high:
        j = partition(a, low, high)
        if j == N//2:
            return a[j]
        elif j < N//2:
            low = j + 1
        else:
            high = j - 1
    return a[N//2]


def partition(a, low, high):
    i = low + 1
    j = high
    while i <= j:
        if a[i] < a[low]:
            i += 1
            continue
        if a[j] > a[low]:
            j -= 1
            continue
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[j], a[low] = a[low], a[j]
    return j


if __name__ == '__main__':
    a = [3, 5, 2, 9, 0, 7, 8]
    print(find_middle(a))
