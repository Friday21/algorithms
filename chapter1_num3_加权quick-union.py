"""
教材145页， 加权quick union 算法
输入是一列整数对， 一堆整数p, q可以被理解为“p和q是相连的。”当程序从输入中读取了整数对
p和q时， 如果已知的所有整数对都不能说明p和q是相连的，那么将这一对整数写入到输出中。否则，
忽略p和q这对整数并继续处理下一对输入。

加权quick union 的思路：
1. 记录每个分量的大小
2. union 时总会将分量小的合并到分量大的
"""


class WeightedQuickUnionUF(object):

    def __init__(self, n):
        self.store = list()
        self.sz = list()
        for i in range(n):
            self.store.append(i)
            self.sz.append(1)

    def find(self, p):
        if self.store[p] == p:
            return p
        return self.find(self.store[p])

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        print(p, q)
        if self.sz[p_root] < self.sz[q_root]:
            self.store[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.store[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]


if __name__ == '__main__':
    wq_union = WeightedQuickUnionUF(11)
    wq_union.union(4, 3)
    wq_union.union(3, 8)
    wq_union.union(6, 5)
    wq_union.union(9, 4)
    wq_union.union(2, 1)
    wq_union.union(8, 9)  # 不应被输出
    wq_union.union(5, 0)
    wq_union.union(7, 2)
    wq_union.union(6, 1)
    wq_union.union(1, 0)  # 不应被输出
    wq_union.union(6, 7)  # 不应被输出
