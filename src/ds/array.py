# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-03 09:20pm


class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0

    def deploy_from_list(self, alist):
        '''
        将传入的列表作为self.data的数据（没有构造函数重载的痛苦，只能用成员函数来实现了）
        '''
        self.data = alist
        self.size = len(alist)

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def getCapacity(self):
        return len(self.data)

    def add(self, index, elem):
        '''
        在index位置插入一个元素elem
        '''
        assert 0 <= index <= self.size

        if self.size == len(self.data):
            self._resize(len(self.data) * 2)  # 两倍扩容

        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = elem
        self.size += 1

    def addLast(self, elem):
        self.add(self.size, elem)

    def addFirst(self, elem):
        self.add(0, elem)

    def get(self, index):
        '''
        拿到索引index处的元素
        '''
        assert 0 <= index < self.size
        return self.data[index]

    def getLast(self):
        return self.get(self.size - 1)

    def getFirst(self):
        return self.get(0)

    def set(self, index, elem):
        '''
        将索引index位置的元素设置为elem
        '''
        assert 0 <= index < self.size
        self.data[index] = elem

    def contains(self, elem):
        '''
        查看是否包含元素elem
        '''
        for i in range(self.size):
            if self.data[i] == elem:
                return True
        return False

    def find(self, elem):
        '''
        查找元素elem，并存在相应的索引，不存在返回-1
        '''
        for i in range(self.size):
            if self.data[i] == elem:
                return i
        return -1

    def remove(self, index):
        '''
        删除索引为index处的元素，返回删除的元素的值
        '''
        assert 0 <= index < self.size

        if self.size <= len(self.data) // 4 and len(self.data) // 2 != 0:
            self._resize(len(self.data) // 2)  # 保证装填因子在50%左右。

        ret = self.data[index]
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]
        self.size -= 1
        return ret

    def removeLast(self):
        return self.remove(self.size - 1)

    def removeFirst(self):
        return self.remove(0)

    def removeElement(self, elem):
        '''
        删除元素elem，如果不存在elem，什么也不做。如果elem的数量多于
        1，那么只删除最左边的一个
        '''
        index = self.contains(elem)
        if index != -1:
            self.remove(index)

    def swap(self, index1, index2):
        '''
        交换索引index1和index2上的元素
        '''
        assert 0 <= index1 < self.size and 0 <= index2 < self.size, \
            'invalid index'
        self.data[index1], self.data[index2] = \
            self.data[index2], self.data[index1]

    def printArray(self):
        for index in range(self.getSize()):
            elem = self.data[index]
            if index != len(self.data) - 1:
                print(elem, end=', ')
            else:
                print(elem)
        print(
            'size: {}, capacity: {}'.format(self.size, len(self.data))
        )

    # private
    def _resize(self, new_capacity):
        '''
        扩容操作，size不变，capacity也不用动，因为是用len(self.data)来
        求的
        '''
        assert self.size <= new_capacity
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data