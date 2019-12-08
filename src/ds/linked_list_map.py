# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-07 1:11pm


class Node:
    def __init__(self, k=None, v=None, next=None):
        self.k = k
        self.v = v
        self.next = next


class LinkedListMap:
    def __init__(self):
        self.dummy_head = Node()
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, k, v):
        '''
        向map中添加k, v键值对
        如果k已经存在，则认为是对这个k的更新value的操作
        '''
        node = self._getNode(k)
        if node is None:
            self.dummy_head.next = Node(k, v, self.dummy_head.next)
            self.size += 1
        else:
            node.v = v

    def contains(self, k):
        '''
        查询map中是否包含键为k的键值对
        '''
        return self._getNode(k) is not None

    def get(self, k):
        '''
        查询键为k的value值
        不存在的话返回None
        '''
        node = self._getNode(k)
        return node.v if node is not None else None

    def set(self, k, v):
        '''
        将键为k的node的v设为v
        前提是用户已经明确知道了k一定在map中
        '''
        node = self._getNode(k)
        if node is None:
            raise Exception('No key:"{}" in current map'.format(k))
        else:
            node.v = v

    def remove(self, k):
        '''
        删除map中键为k的node
        如果k不存在，什么也不做
        返回键为k的节点的v值
        '''
        prev = self.dummy_head
        while prev.next is not None:
            if prev.next.k == k:
                del_node = prev.next
                prev.next = del_node.next
                del_node.next = None
                self.size -= 1
                return del_node.v
            prev = prev.next

    def print(self):
        if self.isEmpty():
            print('Empty map')
        cur = self.dummy_head.next
        while cur is not None:
            print('{}: {}'.format(cur.k, cur.v), end=', ')
            cur = cur.next
        print()
        print('size: {}'.format(self.getSize()))

    # private
    def _getNode(self, k):
        '''
        根据k查找某一个节点，并将这个节点返回。
        如果这个节点不存在，返回None
        '''
        cur = self.dummy_head.next
        while cur is not None:
            if cur.k == k:
                return cur
            cur = cur.next
        return None