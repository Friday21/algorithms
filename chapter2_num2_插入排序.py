"""
教材157页， 插入排序
对于1到N-1之间的每一个i， 将a[i]与a[0]到a[i-1]中比它小的所有元素依次有序地交换。
在索引i由左向右变化的过程中，它左侧的元素总是有序的， 所以到达数组的右端时排序就完成了。

对于随机排列的长度为N且主键不重复的数组， 平均情况下插入排序需要 N^2/4 次比较以及 N^2/4 次交换。
最坏情况下需要 N^2/2 次比较和 N^2/2 次交换， 最好情况下需要 N-1 次比较和 0 次交换。
"""


def quick_sort(input_list):
    length = len(input_list)
    for i in range(1, length):
        for j in range(i-1, -1, -1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
            else:
                break

    return input_list


if __name__ == '__main__':
    unsort = [2, 4, 8, 1, 9, 0]
    print(quick_sort(unsort))
