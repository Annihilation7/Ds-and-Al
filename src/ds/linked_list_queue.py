# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-07 12:57pm


class Node:
    def __init__(self, _data=None, _next=None):
        self.data = _data
        self.next = _next


class LinkedListQueue:
    def __init__(self):
        '''
        链表加入尾节点，达到前面实现的循环队列的性能，头节点和尾节点是左闭右闭区间
        链表头出队，链表尾入队
        这里的实现不带有dummyhead
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, elem):
        '''
        将元素elem入队，需要特殊考虑的情况是size=0的时候
        '''
        if self.size == 0:
            self.head = Node(elem)
            self.tail = self.head
        else:
            self.tail.next = Node(elem)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        '''
        队首元素出队，并返回出队元素的值。
        需要考虑的特殊情况一个是空的时候，另一个是只有一个元素的时候，因为一个元素的时候
        head和tail指向的是同一个元素
        '''
        assert not self.isEmpty(), 'Empty queue.'
        retnode = self.head
        self.head = self.head.next
        retnode.next = None  # 和链表彻底断开联系
        if self.size == 0:
            self.tail = None  # 只有一个元素的时候删完为空，而tail还指着retnode，所以
            # 需要进行维护
        self.size -= 1
        return retnode.data

    def getFront(self):
        '''
        看一下队首元素是谁
        '''
        assert not self.isEmpty(), 'Empty queue.'
        return self.head.data

    def print(self):
        if self.isEmpty():
            print('Empty')
            return
        print('Head:', end=' ')
        cur = self.head
        while cur:
            print(cur.data, end=', ')
            cur = cur.next
        print(': Tail')
        print('Size: {}'.format(self.getSize()))
