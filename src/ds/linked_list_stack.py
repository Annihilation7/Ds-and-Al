# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-07 04:32am


from src.ds.linked_list import LinkedList


class LinkedListStack:
    def __init__(self):
        '''
        由于在链表头的操作都是O(1)的，所以将链表头当作栈顶
        '''
        self.data = LinkedList()

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def push(self, elem):
        self.data.addFirst(elem)

    def pop(self):
        return self.data.removeFirst()

    def peek(self):
        return self.data.getFirst()

    def print(self):
        print('top:', end=' ')
        cur = self.data.dummyhead.next
        while cur is not None:
            print(cur.data, end=', ')
            cur = cur.next
        print(':bottom')