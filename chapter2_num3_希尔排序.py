"""
教材162页， 希尔排序
希尔排序是一种基于插入排序的快速排序算法。核心思想是短的数组或者部分有序的数组更适合插入排序
希尔排序的思想是使数组中任意间隔为h的元素都是有序的(h有序数组)，然后逐步减小h， 对于任意以1为
结尾的h序列， 我们都能够将数组排序。

下面实现的希尔排序， 在最坏的情况下比较次数和 N^(3/2) 成正比。

1. 找到h=3*n +1 且 h < N的最大h.
2. 将数组a[N] 以间隔h分成多个子数组
3. 对每个子数组进行插入排序
4. h = h//3, 重复步骤2， 3
5. h=1 时排序完成
"""


def shell_sort(input_list):
    length = len(input_list)
    h = 1
    while h < length//3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, length):
            j = i - h
            while j >= 0:
                if input_list[j] > input_list[j+h]:
                    input_list[j], input_list[j+h] = input_list[j+h], input_list[j]
                    j -= h
                else:
                    break

        h = h//3
    return input_list


if __name__ == '__main__':
    unsort = [3, 5, 1, 2, 7, 4, 9, 8, 0]
    print(shell_sort(unsort))
