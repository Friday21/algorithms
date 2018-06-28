"""
教材 250页， 二叉查找树
"""


class BinarySearchTree:

    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key, value, num):
            self.key = key
            self.value = value
            self.num = num
            self.left = None
            self.right = None

    def size(self):
        return self.node_size(self.root)

    @classmethod
    def node_size(cls, node):
        if not node:
            return 0
        return node.num

    def get(self, key):
        return self.node_get(self.root, key)

    @classmethod
    def node_get(cls, node, key):
        if not node:
            return None
        if node.key == key:
            return node.value
        elif node.key > key:
            return cls.node_get(node.left, key)
        else:
            return cls.node_get(node.right, key)

    def put(self, key, value):
        self.root = self.node_put(self.root, key, value)

    @classmethod
    def node_put(cls, node, key, value):
        if not node:
            return cls.Node(key, value, 1)
        if key == node.key:
            node.value = value
        elif key > node.key:
            node.right = cls.node_put(node.right, key, value)
        else:
            node.left = cls.node_put(node.left, key, value)

        node.num = cls.node_size(node.left) + cls.node_size(node.right) + 1
        return node

    def min(self):
        return self.node_min(self.root).key

    @classmethod
    def node_min(cls, node):
        if not node.left:
            return node
        return cls.node_min(node.left)

    def floor(self, key):
        node = self.node_floor(self.root, key)
        if not node:
            return None
        return node.key

    @classmethod
    def node_floor(cls, node, key):
        if not node:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return cls.node_floor(node.left, key)
        else:
            return cls.node_floor(node.right, key) or node

    def select(self, k):
        return self.node_select(self.root, k)

    @classmethod
    def node_select(cls, node, k):
        if not node:
            return None
        left_size = cls.node_size(node.left)
        if left_size == k:
            return node
        elif left_size > k:
            return cls.node_select(node.left, k)
        else:
            return cls.node_select(node.right, k-left_size-1)

    def rank(self, key):
        return self.node_rank(self.root, key)

    @classmethod
    def node_rank(cls, node, key):
        if not node:
            return 0
        if node.key == key:
            return cls.node_size(node.left)
        elif node.key > key:
            return cls.node_rank(node.left, key)
        else:
            return cls.node_size(node.left) + 1 + cls.node_rank(node.right, key)

    def delete_min(self):
        self.root = self.node_delete_min(self.root)

    @classmethod
    def node_delete_min(cls, node):
        if not node.left:
            return node.right
        node.left = cls.node_delete_min(node.left)
        node.num = cls.node_size(node.left) + cls.node_size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self.node_delete(self.root, key)

    @classmethod
    def node_delete(cls, node, key):
        if not node:
            return None
        if node.key < key:
            node.right = cls.node_delete(node.right, key)
        elif node.key > key:
            node.left = cls.node_delete(node.left, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            t = node
            node = cls.node_min(t.right)
            node.left = t.left
            node.right = cls.node_delete_min(t.right)

        node.num = cls.node_size(node.left) + cls.node_size(node.right) + 1
        return node

    def keys(self, low, high):
        queue = []
        self.node_keys(self.root, queue, low, high)
        return queue

    @classmethod
    def node_keys(cls, node, queue, low, high):
        if not node:
            return None
        if low <= node.key <= high:
            queue.append(node.key)
        if node.key < high:
            cls.node_keys(node.right, queue, low, high)
        if node.key > low:
            cls.node_keys(node.left, queue, low, high)
