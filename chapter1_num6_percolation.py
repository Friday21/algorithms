"""
教程第一周作业: 提交的java版本在percolation.zip里
http://coursera.cs.princeton.edu/algs4/assignments/percolation.html
Write a program to estimate the value of the percolation threshold via Monte Carlo simulation.
"""
import sys
import random

import numpy as np


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
        if self.sz[p_root] < self.sz[q_root]:
            self.store[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.store[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Percolation(object):

    def __init__(self, n):
        # 0 代表最上层一个点, n*n +1 代表最下层一个点
        # row, col 对应的点序号为n*(row-1) + col
        self.union_find = WeightedQuickUnionUF(n*n + 2)
        self.site = [0] * (n*n + 2)  # 0代表closed, 1 代表opened
        self.num = n
        self.open_num = 0
        for i in range(1, n+1):
            self.union_find.union(0, i)
            self.union_find.union(n*n+1, n*n+1-i)

    def open(self, row, col):
        # union 相邻的四个点中为open的site
        if self.is_open(row, col):
            return
        self.open_num += 1
        index = self.cal_index(row, col)
        self.site[index] = 1
        if row - 1 > 0 and self.is_open(row-1, col):
            index_up = self.cal_index(row-1, col)
            self.union_find.union(index, index_up)
        if row + 1 <= self.num and self.is_open(row+1, col):
            index_down = self.cal_index(row+1, col)
            self.union_find.union(index, index_down)
        if col - 1 > 0 and self.is_open(row, col-1):
            index_left = self.cal_index(row, col-1)
            self.union_find.union(index, index_left)
        if col + 1 <= self.num and self.is_open(row, col+1):
            index_right = self.cal_index(row, col+1)
            self.union_find.union(index, index_right)

    def is_open(self, row, col):
        index = self.cal_index(row, col)
        return self.site[index] == 1

    def is_full(self, row, col):
        index = self.cal_index(row, col)
        return self.site[index] == 0

    def num_of_open_site(self):
        return self.open_num

    def is_percolate(self):
        return self.union_find.is_connected(0, self.num * self.num + 1)

    def cal_index(self, row, col):
        return self.num * (row - 1) + col

    def random_open_until_percolate(self):
        while not self.is_percolate():
            row = random.randint(1, self.num)
            col = random.randint(1, self.num)
            self.open(row, col)


class PercolationStats(object):
    def __init__(self, n, t):
        self.num = n
        self.test_time = t
        self.probability = []
        for i in range(t):
            percolation = Percolation(n)
            percolation.random_open_until_percolate()
            self.probability.append(percolation.open_num/(n*n))
        self.np = np.array(self.probability)

    def mean(self):
        return self.np.mean()

    def stddev(self):
        return self.np.var()

    def confidence_lo(self):
        return self.mean() - 1.96 * self.stddev() / np.sqrt(self.test_time)

    def confidence_hi(self):
        return self.mean() + 1.96 * self.stddev() / np.sqrt(self.test_time)


if __name__ == '__main__':
    n = int(sys.argv[1])
    t = int(sys.argv[2])
    percolation_stats = PercolationStats(n, t)
    print('mean: {}'.format(percolation_stats.mean()))
    print('stddev: {}'.format(percolation_stats.stddev()))
    print('95% confidence interval: [{}, {}]'.format(
        percolation_stats.confidence_lo(), percolation_stats.confidence_hi()))