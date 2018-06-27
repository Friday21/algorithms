"""
教程第一周练习题: Successor with delete
Successor with delete. Given a set of nn integers S={0,1,...,n−1} and a sequence
of requests of the following form:

Remove x from S
Find the successor of x: the smallest y in S such that y≥x.

design a data type so that all operations (except construction)
take logarithmic time or better in the worst case.

思路:
初始化, store[i]为i本身, sz[i]为1, successor[i]为i
remove x, 相当于union x 和 x + 1, successor[x] 和 successor[x+1] 记录为两者较大的值
find successor of x,  find_root, 返回successor[root]
"""


class Successor(object):

    def __init__(self, n):
        self.store = list()
        self.sz = list()
        self.successor = list()
        for i in range(n):
            self.store.append(i)
            self.sz.append(1)
            self.successor.append(i)

    def root(self, p):
        if self.store[p] == p:
            return p
        return self.root(self.store[p])

    def remove(self, x):
        p = x
        q = x + 1
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return
        if self.sz[p_root] < self.sz[q_root]:
            self.store[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.store[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]

        if self.successor[p_root] > self.successor[q_root]:
            self.successor[q_root] = self.successor[p_root]
        else:
            self.successor[p_root] = self.successor[q_root]

    def find_successor(self, x):
        root = self.root(x)
        return self.successor[root]


if __name__ == '__main__':
    successor = Successor(10)
    successor.remove(3)
    print(successor.find_successor(3))
    successor.remove(5)
    print(successor.find_successor(5))
