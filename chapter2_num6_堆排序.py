"""
教材205 堆排序
1. 构造一个最大值堆N(如果一个结点的两个子结点都已经是堆了， 那么在该结点上调用
sink 可以将它们变成一个堆)
2. 把堆的顶端和末端交换， 排序堆N-1
3. 输出数组

将N个元素排序， 堆排序只需少于(2NlgN + 2N)次比较， 以及一半次数的交换。
堆排序可以用来处理大规模数据的排序（内存装不小的情况）
"""


def heap_sort(input_list):
    # 1. 构造堆
    n = len(input_list)
    input_list.insert(0, 0)  # 堆从a[1]开始
    for k in range(n//2, 0, -1):
        sink(input_list, k, n)

    # 2. 去掉堆顶， 重新排序
    for i in range(n, 0, -1):
        input_list[i], input_list[1] = input_list[1], input_list[i]
        sink(input_list, 1, i-1)

    input_list.pop(0)


def sink(a, k, n):
    while 2 * k <= n - 1:
        j = 2 * k
        if a[j] < a[j+1]:
            j += 1
        if a[k] < a[j]:
            a[k], a[j] = a[j], a[k]
            k = j
        else:
            break


if __name__ == '__main__':
    unsort = [3, 6, 5, 7, 2, 1, 9, 8, 0]
    heap_sort(unsort)
    print(unsort)
