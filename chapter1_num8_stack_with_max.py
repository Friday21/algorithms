"""
教程第二周思考题：
Stack with max. Create a data structure that efficiently supports the stack operations (push and pop) and also
a return-the-maximum operation. Assume the elements are reals numbers so that you can compare them.
"""


class Stack(object):
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.max = 0

    def push(self, value):
        self.stack.append(value)
        self.max = max(self.max, value)
        self.max_stack.append(self.max)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def max(self):
        return self.max_stack[-1]

    def is_empty(self):
        return bool(self.stack)
