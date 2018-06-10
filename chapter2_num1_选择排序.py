"""
教材155页， 选择排序（冒泡法）
1. 首先， 找到数组中最小的那个元素
2. 其次， 将它和数组的第一个元素交换
3. 再次， 在剩下的元素中找到最小的元素， 将它和数组的第二个元素交换位置
4. 如此往复， 直到将整个数组排序
选择排序需要大约 N^3/2 次比较和N次交换
"""


def choose_sort(input_list):
    length = len(input_list)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list


if __name__ == '__main__':
    unsort = [4, 7, 3, 2, 9, 1]
    sort = choose_sort(unsort)
    print(sort)
