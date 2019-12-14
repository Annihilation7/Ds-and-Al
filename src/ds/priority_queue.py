# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 03:24pm


from src.ds.max_heap import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.data = MaxHeap()

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def enqueue(self, elem):
        '''
        将元素elem加入到优先队列中
        '''
        self.data.add(elem)

    def getFront(self):
        '''
        看一下优先队列的队首元素是谁
        '''
        return self.data.find_max()

    def dequeue(self):
        '''
        将优先队列的队首元素出队
        返回出队的元素
        '''
        return self.data.extractMax()

    def print(self):
        if self.isEmpty():
            print('Empty priority queue')
            return
        print('Head: ', end='')
        for index in range(self.getSize()):
            print(self.data.data.data[index], end=', ')
        print(f':Tail ----- Size: {self.getSize()}')