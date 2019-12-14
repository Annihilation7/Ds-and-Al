# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 02:27am


from src.ds.array import Array


class MaxHeap:
    def __init__(self, capacity=10):
        '''
        是完全二叉树，不一定是满二叉树
        本节实现最大堆，最小堆大同小异
        数组索引从0开始
        可以用最大堆实现一个完美的优先队列
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

    def find_max(self):
        '''
        找到最大堆中最大的元素（队首的元素）
        '''
        if self.data.isEmpty():
            raise Exception('Empty Maxhep.')
        return self.data.get(0)

    def extractMax(self):
        '''
        抽取出最大堆中最大的元素
        '''
        ret = self.find_max()
        self.data.swap(0, self.getSize() - 1)
        self.data.removeLast()
        self._shiftDown(0)
        return ret

    def replace(self, elem):
        '''
        将最大元素删除，然后添加元素elem
        返回删除的最大元素
        很自然的想法是先extractMax，然后add(elem) 两次O(logn)
        可以优化成1次：将最大元素直接替换成elem，然后shiftDown就可以了。
        '''
        ret = self.find_max()
        self.data.set(0, elem)
        self._shiftDown(0)
        return ret

    def heapify(self, alist):
        '''
        传入一个列表，将列表中的元素变成以最大堆的方式存储，同时更新self.data
        很自然的想法就是遍历，然后add，时间复杂度为 O(nlogn)
        有更好的方法：从最后一个有叶子节点的跟节点开始往前一直到root，调用shiftDown就可以
            完成最大堆的维护了，时间复杂度是O(n)
        '''
        self.data.deploy_from_list(alist)
        for i in range(self._parent(self.data.getSize() - 1), -1, -1):
            self._shiftDown(i)

    def print(self):
        self.data.printArray()

    def _parent(self, index):
        '''
        根据当前索引求index的父亲索引
        '''
        assert index != 0, 'Root node has no parent node.'
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

    def _shiftDown(self, index):
        '''
        将当前索引index上的元素进行下沉操作
        '''
        while self._left_child(index) < self.getSize():
            # j代表了孩子节点中最大元素的索引
            j = self._left_child(index)
            if (j + 1 < self.getSize()) and \
                (self.data.get(j + 1) > self.data.get(j)):
                j += 1
            if self.data.get(j) < self.data.get(index):
                break
            self.data.swap(index, j)
            index = j