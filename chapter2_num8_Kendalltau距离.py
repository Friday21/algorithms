"""
教材 225页， 在线性对数时间内计算两组排列之间的 Kendall tau 距离

参考：
    http://shmilyaw-hotmail-com.iteye.com/blog/2275113
    http://shmilyaw-hotmail-com.iteye.com/blog/1769047

1. 建立a的索引映射anti_a
2. 根据anti_a 建立b对应a的索引anti_b
3. 用归并排序计算anti_b的反序对数
"""
count = 0


def kt_distance(a, b):
    if len(a) != len(b):
        raise ValueError('a 和 b 两数组长度应该相等')
    length = len(a)
    anti_a = [None] * length
    for index, value in enumerate(a):
        anti_a[value] = index
    anti_b = [None] * length
    for i in range(length):
        anti_b[i] = anti_a[b[i]]
    return cal_inversion(anti_b)


def cal_inversion(input_list):
    m_sort = MergeSort(input_list)
    m_sort.sort()
    return m_sort.count


class MergeSort(object):

    def __init__(self, input_list):
        self.input_list = input_list  # 只是引用
        self.temp_list = [value for value in input_list]  # 新建一个等值数组
        self.count = 0

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
                self.count += mid - i + 1
                self.input_list[k] = self.temp_list[j]
                j += 1

    def sort(self, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(self.input_list) - 1
        if low >= high:
            return
        mid = low + (high - low) // 2
        self.sort(low, mid)
        self.sort(mid+1, high)
        self.merge(low, mid, high)

    def result(self):
        self.sort()
        return self.input_list


if __name__ == '__main__':
    a = [0, 3, 1, 6, 2, 5, 4]
    b = [1, 0, 3, 6, 4, 2, 5]
    print(kt_distance(a, b))
