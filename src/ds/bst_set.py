# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 12:27pm


from src.ds.bst import BST


class SetBst:
    def __init__(self):
        '''
        不包含重复元素
        前面实现的bst天然支持集合的各种操作
        '''
        self.data = BST()

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def contains(self, elem):
        '''
        查询集合中是否包含元素elem
        '''
        return self.data.contains(elem)

    def add(self, elem):
        '''
        向集合中添加元素
        '''
        self.data.add(elem)

    def remove(self, elem):
        '''
        删除元素elem
        '''
        self.data.remove(elem)

    def print(self):
        '''
        打印集合，这里采用层序遍历的方式打印
        '''
        self.data.levelOrder()