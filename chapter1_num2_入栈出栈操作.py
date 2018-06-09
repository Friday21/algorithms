"""
教材101页， 练习题1.3.3
假设某个用例程序会进行一系列入栈和出栈的混合栈操作。入栈操作会将整数0到9按顺序压入栈；
出栈操作会打印出返回值。判断哪种序列是不可能产生的

思路：
1. 一个数字打印出来， 那么比它小的数字肯定都已经入栈了
2. 一个数字打印出来， 那么栈内不能有比它大的数字
"""


def is_stack_operate_possible(result):
    stack = []
    out_stack = []  # 已经出站的数字， 不能再入站
    for num in result:
        for big_num in range(num+1, 10):
            if big_num in stack:
                print(num, big_num)
                return False
        out_stack.append(num)
        if stack and stack[-1] == num:
            stack.pop()
            continue
        for little_num in range(num):
            if little_num not in out_stack and little_num not in stack:
                stack.append(little_num)
    return True


if __name__ == '__main__':
    print(is_stack_operate_possible([4, 3, 2, 1, 0, 9, 8, 7, 6, 5]))
    print(is_stack_operate_possible([4, 6, 8, 7, 5, 3, 2, 9, 0, 1]))
    print(is_stack_operate_possible([2, 5, 6, 7, 4, 8, 9, 3, 1, 0]))
    print(is_stack_operate_possible([4, 3, 2, 1, 0, 5, 6, 7, 8, 9]))
    print(is_stack_operate_possible([1, 2, 3, 4, 5, 6, 9, 8, 7, 0]))
    print(is_stack_operate_possible([0, 4, 6, 5, 3, 8, 1, 7, 2, 9]))
    print(is_stack_operate_possible([1, 4, 7, 9, 8, 6, 5, 3, 0, 2]))
    print(is_stack_operate_possible([2, 1, 4, 3, 6, 5, 8, 7, 9, 0]))
