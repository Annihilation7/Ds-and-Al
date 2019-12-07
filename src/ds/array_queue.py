# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-06 12:43am


from src.ds.array import Array


class ArrayQueue:
    def __init__(self, capacity=10):
        self.data = Array(capacity)

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def getCapacity(self):
        return self.data.getCapacity()

    def enqueue(self, elem):
        '''
        入队一个元素，对首在数组头部，队尾为数组尾部
        '''
        self.data.addLast(elem)

    def dequeue(self):
        '''
        出队一个元素，并将其返回
        '''
        return self.data.removeFirst()

    def getFront(self):
        '''
        看一眼队首的元素是谁
        '''
        return self.data.getFirst()

    def printQueue(self):
        print('Tail:', end=' ')
        for i in range(self.getSize()):
            if i != self.getSize() - 1:
                print(self.data.get(i), end=', ')
            else:
                print(self.data.get(i), end=' Head\n')