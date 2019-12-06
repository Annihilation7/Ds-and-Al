# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-07 03:00pm


class Node:
    def __init__(self, _data=None, _next=None):
        self.data = _data
        self.next = _next


class LinkedList:
    def __init__(self):
        '''
        能做到真正的动态
        add和remove操作真正关心的是"目标索引"的前一个Node
        '''
        self.dummyhead = Node()
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, index, elem):
        '''
        在"索引index"处添加元素elem
        O(n)
        '''
        assert 0 <= index <= self.size, 'Invalid insert index, please check.'
        prev = self.dummyhead
        while index:
            prev = prev.next
            index -= 1
        prev.next = Node(elem, prev.next)
        self.size += 1

    def addFirst(self, elem):
        '''O(1)'''
        self.add(0, elem)

    def addLast(self, elem):
        '''O(n)'''
        self.add(self.size, elem)

    def get(self, index):
        '''
        查看"索引index"位置的元素
        O(n)
        '''
        assert 0 <= index < self.size, 'Invalid get index, please check'
        cur = self.dummyhead.next
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.data

    def getFirst(self):
        '''O(1)'''
        return self.get(0)

    def getLast(self):
        '''O(n)'''
        return self.get(self.size - 1)

    def set(self, index, elem):
        '''
        将"索引index"位置的元素替换成elem
        O(n)
        '''
        assert 0 <= index < self.size, 'Invalid get index, please check'
        cur = self.dummyhead.next
        while index > 0:
            cur = cur.next
            index -= 1
        cur.data = elem

    def contains(self, elem):
        '''
        查看链表中是否包含elem
        O(n)
        '''
        cur = self.dummyhead.next
        while cur is not None:
            if cur.data == elem:
                return True
            cur = cur.next
        return False  # 能够处理链表为空的情况，所以不用单独处理

    def remove(self, index):
        '''
        将"索引index"位置的元素删除，并返回删除的元素
        O(n)
        '''
        assert 0 <= index < self.size, 'Invalid remove index, please check'
        prev = self.dummyhead
        while index:
            prev = prev.next
            index -= 1
        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None  # 准备被自动垃圾回收
        self.size -= 1
        return del_node.data

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self.size - 1)

    def printLinkedList(self):
        if self.size == 0:
            print('Empty')
        prev = self.dummyhead
        while prev.next is not None:
            print(prev.next.data, end=', ')
            prev = prev.next
        print('None')
        print('Size: {}'.format(self.size))