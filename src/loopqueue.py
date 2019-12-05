# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-03 09:20pm


class LoopQueue:
    def __init__(self, capacity=10):
        '''
        capacity是面向使用者来说的，所以这里的真实容量是capacity + 1
        front==tail表示空，(tail+1)%(capacity+1)==front表示满
        '''
        self.data = [None] * (capacity + 1)
        self.head = self.tail = 0  # 其实初始化相等就可以了，为了方便，都放在0索引处
        self.size = 0  # 不想麻烦了，就一个变量而已

    def getCapacity(self):
        return len(self.data) - 1  # 面向客户

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def enqueue(self, elem):
        '''
        将元素入队
        '''
        if self.size == self.getCapacity():
            self._resize(self.getCapacity() * 2)  # 面向客户
        self.data[self.tail] = elem
        self.tail = (self.tail + 1) % len(self.data)
        self.size += 1

    def dequeue(self):
        '''
        将队首元素出对，并返回
        '''
        if self.isEmpty():
            raise Exception('Empty loopqueue.')
        ret = self.data[self.head]
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        if self.size / self.getCapacity() <= 0.25 and self.size // 2 != 0:
            self._resize(self.getCapacity() // 2)
        return ret

    def _resize(self, new_size):
        new_data = [None] * new_size
        for i in range(self.size):
            new_data[i] = self.data[(self.head + i) % len(self.data)]

        self.data = new_data
        self.head = 0
        self.tail = self.size

    def printLoopQueue(self):
        print('Head:', end=' ')
        for i in range(self.size):
            end = ', ' if i != self.size - 1 else ' :Tail\n'
            print(self.data[(self.head + i) % len(self.data)], end=end)
        print(
            'Size: {}, Capacity: {}'.format(self.getSize(), self.getCapacity())
        )