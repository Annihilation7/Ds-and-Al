# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 12:44pm


from src.ds.linked_list import LinkedList


class LinkedListSet:
    def __init__(self):
        self.data = LinkedList()

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def contains(self, elem):
        return self.data.contains(elem)

    def add(self, elem):
        self.data.addFirst(elem)

    def remove(self, elem):
        self.data.removeElement(elem)

    def print(self):
        self.data.printLinkedList()