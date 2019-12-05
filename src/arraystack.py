# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-03 09:20pm


from src.array import Array


class StackArray:
    def __init__(self, capacity=10):
        self.data = Array(capacity)

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def getCapacity(self):
        return self.data.getCapacity()

    def push(self, elem):
        '''
        向栈中推一个元素
        '''
        self.data.addLast(elem)

    def pop(self):
        '''
        删除栈顶元素，返回删除的元素
        '''
        return self.data.removeLast()

    def peek(self):
        '''
        看一下栈顶的元素是谁
        '''
        return self.data.getLast()

    def printStack(self):
        print('bottom [', end=' ')
        for index in range(self.data.size):
            elem = self.data.data[index]
            if index != self.getSize() - 1:
                print(elem, end=', ')
            else:
                print(elem, end=' ] top\n')