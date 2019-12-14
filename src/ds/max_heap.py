# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-14 02:27am


from src.ds.array import Array


class MaxHeap:
    def __init__(self, capacity=10):
        '''
        是完全二叉树，不一定是满二叉树
        本节实现最大堆，最小堆大同小异
        数组索引从0开始
        '''
        self.data = Array(capacity)

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def add(self, elem):
        '''
        向堆中添加元素elem
        shiftUp登场
        '''
        self.data.addLast(elem)
        self._shiftUp(self.data.size - 1)  # 因为已经维护了data的size变量，所以-1

    def print(self):
        self.data.printArray()

    def _parent(self, index):
        '''
        根据当前索引求index的父亲索引
        '''
        assert index != 0, 'Root node has not parent node.'
        return (index - 1) // 2

    def _left_child(self, index):
        '''
        根据当前索引求左孩子的索引
        '''
        return index * 2 + 1

    def _right_child(self, index):
        '''
        根据当前索引求右孩子的索引
        '''
        return index * 2 + 2

    def _shiftUp(self, index):
        '''
        将当前索引index上的元素进行上浮操作
        '''
        while (index > 0) and \
                (self.data.get(index) > self.data.get(self._parent(index))):
            self.data.swap(index, self._parent(index))
            index = self._parent(index)


