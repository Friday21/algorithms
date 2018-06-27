"""
教程第一周练习题: Interview Questions: Union–Find (ungraded)
Social network connectivity: Given a social network containing nn members and a log file
containing mm timestamps at which times pairs of members formed friendships, design an
algorithm to determine the earliest time at which all members are connected (
i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file
is sorted by timestamp and that friendship is an equivalence relation. The running time of your
algorithm should be m*logn or better and use extra space proportional to n.

解法:
加权quick-union, 用sz[i] 记录成员i的朋友数目
当union操作时, 如果sz[i] + sz[j]的数目等于了n, 则证明所有成员都是朋友了, 返回当前时间戳
"""


class SocialNetworkConnect(object):

    def __init__(self, n):
        self.size = n
        self.store = list()
        self.sz = list()
        for i in range(n):
            self.store.append(i)
            self.sz.append(1)

    def root(self, p):
        if self.store[p] == p:
            return p
        return self.root(self.store[p])

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return False

        if self.sz[p_root] < self.sz[q_root]:
            self.store[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.store[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]

        if self.sz[q_root] == self.size or self.sz[p_root] == self.size:
            return True
        return False


if __name__ == '__main__':
    wq_union = SocialNetworkConnect(11)
    with open('chapter1_friend_log.txt', 'r') as f:
        for line in f.readlines():
            time_stamp, member_i, member_j = line.split()
            if wq_union.union(int(member_i), int(member_j)):
                print('all member become friend at time {}'.format(time_stamp))
                break
