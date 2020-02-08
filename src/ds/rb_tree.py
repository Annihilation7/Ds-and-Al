# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-07 03:41am


from src.ds.loop_queue import LoopQueue


RED = True
BLACK = False


class Node:
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None
        self.color = RED  # 默认节点颜色是红色的


class RbTree:
    """
    1. 每个节点或者是红色的，或者是黑色的。
    2. 根节点是黑色的。
    3. 每一个叶子节点（最后的空节点）是黑色的。
    4. 如果一个节点是红色的，那么它的孩子节点都是黑色的。
    5. 从任意一个节点到叶子节点，经过的黑色节点是一样的。（一定要注意是 黑色）。
    本质上是保持"黑平衡"的二叉树，而不是严格意义上的平衡二叉树。最大高度：2(logN)

    红黑树在添加、删除操作上的性能要比avl树的效率要高。如果查询操作比较多，那么avl树
    效率更高一些。但是综合来看，红黑树的统计性能更优！

    本节只实现添加操作，其他的除了删除操作都和以前的bst的实现方法是一样的，但是不实现
    删除操作了，比较复杂……
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def is_red(self, node):
        if node is None:
            return BLACK  # 如果是None则返回Black，因为这里谈不上什么融合
        return node.color

    def print(self):
        """广度优先遍历"""
        if self.isEmpty():
            print('Empty RbTree.')
        q = LoopQueue()
        q.enqueue(self.root)
        while not q.isEmpty():
            node = q.dequeue()
            print('(value: {}, color: {})'.format(
                node.data, '红' if node.color else '黑'
            ), end=', ')
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    def add(self, elem):
        self.root = self._add(self.root, elem)
        self.root.color = BLACK  # 根节点一定是黑色

    def _left_rotate(self, node):
        """
        由于红色节点是左倾斜的，所以有时需要通过左旋转来保持这种性质。
              node                                   x
             /    \                                /   \
            T1     x             ---->           node   T3
                 /   \                          /   \
                T2    T3                       T1   T2
        :param node: 当前子树的根节点
        :return: 新的根节点
        """
        x = node.right
        node.right = x.left
        x.left = node
        # 维护
        x.color = node.color
        node.color = RED

        return x

    def _right_rotate(self, node):
        """
        右旋转
                node                                      x
               /   \                                    /   \
              x     T3           ---->                T1   node
            /  \                                           /  \
           T1  T2                                        T2    T3
        :param node: 当前子树的根节点
        :return: 新的根节点
        """
        x = node.left
        node.left = x.right
        x.right = node
        # 维护
        x.color = node.color
        node.color = RED  # 表示和父亲节点融合在一起

        return x

    def _flip_colors(self, node):
        """
        颜色反转
        :param node: 当前根节点
        """
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def _add(self, node, elem):
        if node is None:
            self.size += 1
            return Node(elem)  # 默认添加的就是红节点

        if node.data < elem:
            node.right = self._add(node.right, elem)
        elif elem < node.data:  # 还是不包含重复元素的
            node.left = self._add(node.left, elem)

        # 注意三个条件不是互斥的，而且是有顺序性的
        if self.is_red(node.right) and not self.is_red(node.left):  # 红节点需要左"倾斜"
            node = self._left_rotate(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self._right_rotate(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self._flip_colors(node)

        return node