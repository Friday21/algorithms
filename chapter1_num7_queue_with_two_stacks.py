"""
教程第二周思考题：
Queue with two stacks. Implement a queue with two stacks so that each queue operations
takes a constant amortized number of stack operations。
https://www.coursera.org/learn/algorithms-part1/quiz/qk8vT/interview-questions-stacks-and-queues-ungraded
"""


class Queue(object):
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if self.stack_out:
            return self.stack_out.pop()
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def is_empty(self):
        return not (self.stack_out or self.stack_in)

