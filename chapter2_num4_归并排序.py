"""
教材170页， 归并排序
将一个数组排序， 可以先递归的将它分成两半分别排序， 然后将结果归并起来。
对于长度为N的任意数组， 自顶向下的归并排序需要1/2NlgN 至 NlgN 次比较
归并排序是一种渐进最优的基于比较排序的算法
"""


class MergeSort(object):

    def __init__(self, input_list):
        self.input_list = input_list  # 只是引用
        self.temp_list = [value for value in input_list]  # 新建一个等值数组

    def merge(self, low, mid, high):
        i = low
        j = mid + 1
        for k in range(low, high+1):
            self.temp_list[k] = self.input_list[k]

        for k in range(low, high+1):
            if i > mid:
                self.input_list[k] = self.temp_list[j]
                j += 1
            elif j > high:
                self.input_list[k] = self.temp_list[i]
                i += 1
            elif self.temp_list[i] < self.temp_list[j]:
                self.input_list[k] = self.temp_list[i]
                i += 1
            else:
                self.input_list[k] = self.temp_list[j]
                j += 1

    def sort(self, low=None, high=None):
        if low >= high:
            return
        mid = low + (high - low) // 2
        self.sort(low, mid)
        self.sort(mid+1, high)
        self.merge(low, mid, high)

    def result(self):
        self.sort(0, len(self.input_list) - 1)
        return self.input_list


if __name__ == '__main__':
    unsort = [3, 5, 1, 2, 7, 4, 9, 8, 0]
    unsort_2 = [3, 5, 1, 2, 7, 4, 9, 8, 0, 6]  # 偶数个

    print(MergeSort(unsort).result())
    print(MergeSort(unsort_2).result())
