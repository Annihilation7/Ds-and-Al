# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-21 05:40pm


class SegmentTree:
    def __init__(self, data, merger):
        self.data = data
        # 开辟至少4倍数组的空间，另外tree对用户来说是不可见的
        # 是一颗完满二叉树，无效元素的位置的填充为None
        # 由于线段树的操作不涉及到增加、删除等改变元素数目的操作，所以定死空间是没有问题的
        self.tree = [None] * 4 * len(self.data)
        # merger是一个融合函数，代表了线段树节点上的值是如何得到的（比如求和函数啊什么的）
        self.merger = merger
        self._build_segmentTree(0, 0, len(self.data) - 1)  # 初始化segmentTree

    def get(self, index):
        assert 0 <= index < len(self.data), 'Invalid index.'
        return self.data[index]

    def getSize(self):
        return len(self.data)

    def query(self, l, r):
        '''
        查询数组中[l, r]区间上merger的结果（比如求和）
        '''
        assert 0 <= l <= r < self.getSize(), 'Invalid indexes.'
        return self._query(0, 0, self.getSize() - 1, l, r)

    def set(self, index, e):
        '''
        将数组中index位置的元素替换为e
        '''
        assert 0 <= index < self.getSize(), 'invalid index.'
        self.data[index] = e  # 更新数组
        self._set(0, 0, self.getSize() - 1, index, e)  # 更新tree

    def print(self):
        print('data: ', end='')
        for i in range(self.getSize()):
            print(self.data[i], end=', ')
        print()
        print('tree_data: ', end='')
        for i in range(4 * self.getSize()):
            print(self.tree[i], end=', ')
        print()

    def _left_child(self, index):
        '''
        获取左孩子的index
        '''
        return index * 2 + 1

    def _right_child(self, index):
        '''
        获取右孩子的index
        '''
        return index * 2 + 2

    def _build_segmentTree(self, tree_index, l, r):
        '''
        从树中tree_index的位置构建区间为[l, r]的线段树
        :param tree_index: 线段树中的起始索引
        :param l: 数组中的左索引
        :param r: 数组中的右索引
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return

        # 构建左、右树
        left_child = self._left_child(tree_index)
        right_child = self._right_child(tree_index)
        mid = l + (r - l) // 2
        self._build_segmentTree(left_child, l, mid)
        self._build_segmentTree(right_child, mid + 1, r)

        # 回溯
        self.tree[tree_index] = self.merger(
            self.tree[left_child], self.tree[right_child]
        )

    def _query(self, tree_index, l, r, query_l, query_r):
        '''
        在以tree_index为根节点的线段树中查找data中[query_l, query_r]区间上的merger结果
        :param tree_index: 当前线段树的根节点索引
        :param l: 当前线段树根节点所代表的区间左边界
        :param r: 当前线段树根节点所代表的区间右边界
        :param query_l: 查询区间的左边界
        :param query_r: 查询区间的右边界
        '''
        if l == query_l and r == query_r:
            return self.tree[tree_index]

        left_child = self._left_child(tree_index)
        right_child = self._right_child(tree_index)
        mid = l + (r - l) // 2

        # 三种查找情况
        # 注意 tree_index代表的区间是[l, r]，所以两个孩子的区间的分别是
        # [l, mid], [mid + 1, r]，所以是下面的两个判断条件。
        if query_r < mid + 1:
            return self._query(left_child, l, mid, query_l, query_r)
        elif mid < query_l:
            return self._query(right_child, mid + 1, r, query_l, query_r)

        left_result = self._query(left_child, l, mid, query_l, mid)
        right_result = self._query(right_child, mid + 1, r, mid + 1, query_r)
        return self.merger(left_result, right_result)

    def _set(self, tree_index, l, r, index, e):
        '''
        在以tree_index为根节点的线段树中将数组中的index位置设为e后的更新树的操作
        :param tree_index: 当前线段树的根节点索引
        :param l: 当前线段树根节点所代表的区间左边界
        :param r: 当前线段树根节点所代表的区间右边界
        :param index: 数组中的索引
        :param e: 替换元素
        '''
        if l == r:
            self.tree[tree_index] = e
            return

        left_child = self._left_child(tree_index)
        right_child = self._right_child(tree_index)
        mid = l + (r - l) // 2

        if index <= mid:
            self._set(left_child, l, mid, index, e)
        else:
            self._set(right_child, mid + 1, r, index, e)

        # 回溯，因为改变了叶子节点的元素值，所以非叶子节点所代表的值已经不对了
        self.tree[tree_index] = self.merger(
            self.tree[left_child], self.tree[right_child]
        )