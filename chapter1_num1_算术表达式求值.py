"""
教材79页， 用两个栈实现算术运算操作。 步骤如下：
1. 将操作数压入操作数栈
2. 将运算符压入运算符栈
3. 忽略左括号
4. 在遇到右括号时， 弹出一个运算符， 弹出所需数量的操作数， 并将运算符和操作数的运算结果压入操作数栈。

注： 这只是一个简单实现， 假定输入的算术表达式运算的逻辑全部都被括号包括了起来。
"""


def calculate_expr(expression):
    operator_stack = []
    value_stack = []
    for s in expression:
        if s == '(' or s == ' ':
            continue
        elif s in '0123456789':
            value_stack.append(int(s))
        elif s in '+-*/':
            operator_stack.append(s)
        elif s == ')':
            oper = operator_stack.pop()
            value1 = value_stack.pop()
            value2 = value_stack.pop()
            if oper == '+':
                value_stack.append(value2 + value1)
            elif oper == '-':
                value_stack.append(value2 - value1)
            elif oper == '*':
                value_stack.append(value2 * value1)
            elif oper == '/':
                value_stack.append(value2 / value1)
            else:
                raise ValueError('不支持的操作符：{}'.format(oper))
        else:
            raise ValueError('不支持的字符：{}'.format(s))

    return value_stack.pop()


if __name__ == '__main__':
    expr = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'
    result = calculate_expr(expr)
    print('{} 的计算结果是：{}'.format(expr, result))
    assert 101 == result
