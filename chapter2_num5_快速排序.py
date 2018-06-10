"""
教材182页， 快速排序(循环和递归中的边界要仔细处理)
快速排序是一种分治的排序算法。它将一个数组分成两个子数组， 将两部分独立的排序
该方法的关键在于切分， 这个过程需要满足三个条件：
1. 对于j, a[j] 已经排定
2. a[low] 到 a[j-1]中的所有元素都不大于a[j]
3. a[j+1] 到 a[high]中的元素都不小于a[j]

切分的思路如下：
1. 先随意的取a[low]作为切分元素
2. 从数组的左端开始扫描， 直到找到一个大于等于它的元素
3. 从数组的右端开始扫描， 直到找到一个小宇等于它的元素
4. 交换两个元素的位置
5. 两个指针相遇时， 将切分元素a[low]和左子数组最右侧的元素a[j]交换，然后返回j

快速排序是原地排序， 且将长度为N的数组排序所需要的时间和NlgN成正比。 将长度为N的无
重复数组排序， 快速排序平均需要 2NlnN（1.39NlgN）次比较, 最多需要N^2 / 2 次
比较（但随机打乱数组能预防这种情况）
"""


def quick_sort(input_list, low, high):
    if low >= high:
        return
    location = partition(input_list, low, high)
    quick_sort(input_list, low, location-1)
    quick_sort(input_list, location+1, high)


def partition(input_list, low, high):
    i = low + 1
    j = high
    while i <= j:
        if input_list[i] < input_list[low]:
            i += 1
            continue
        if input_list[j] > input_list[low]:
            j -= 1
            continue
        input_list[i], input_list[j] = input_list[j], input_list[i]
        i += 1
        j -= 1

    input_list[j], input_list[low] = input_list[low], input_list[j]
    return j


if __name__ == '__main__':
    unsort = [3, 6, 5, 7, 2, 1, 9, 8, 0]
    quick_sort(unsort, 0, len(unsort)-1)
    print(unsort)
