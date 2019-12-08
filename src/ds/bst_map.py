# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-07 02:03pm


from src.ds.loop_queue import LoopQueue


class Node:
    def __init__(self, k=None, v=None, left=None, right=None):
        self.k = k
        self.v = v
        self.left = left
        self.right = right


class BstMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def contains(self, k):
        '''
        map中是否包含键k
        '''
        node = self._getNode(self.root, k)
        return True if node is not None else False

    def add(self, k, v):
        '''
        向map中添加k, v键值对。
        若k已经存在，则认为是对该键值对的更新操作
        '''
        self.root = self._add(self.root, k, v)

    def get(self, k):
        '''
        查询键为k的value值
        不存在的话返回None
        '''
        node = self._get(self.root, k)
        return node.v if node is not None else None

    def set(self, k, v):
        '''
        将键为k的node的v设为v
        前提是用户已经明确知道了k一定在map中
        '''
        self._set(self.root, k, v)

    def remove(self, k):
        '''
        删除map中键为k的节点
        返回map中携带键k的value
        也是用"后继"节点来实现
        若k不存在，返回None
        '''
        node = self._get(self.root, k)
        if node is not None:
            self.root = self._remove(self.root, k)
            return node.v
        return None

    def print(self):
        '''
        这里选择levelorder打印方式
        '''
        if self.isEmpty():
            print('empty map')
            return
        queue = LoopQueue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            node = queue.dequeue()
            print('{}: {}'.format(node.k, node.v), end=', ')
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        print()
        print('size: {}'.format(self.getSize()))

    # private
    def _getNode(self, node, k):
        '''
        查找以node为根的map中携带键为k的节点
        没找到返回None
        '''
        if node is None:
            return None
        if node.k < k:
            return self._getNode(node.right, k)
        elif k < node.k:
            return self._getNode(node.left, k)
        else:
            return node

    def _add(self, node, k, v):
        '''
        向以node为根的map中添加k，v键值对
        返回添加键值对后的map的新的根节点
        若k已经存在，则认为是对该键值对的更新操作
        '''
        if node is None:
            self.size += 1
            return Node(k, v)

        if node.k < k:
            node.right = self._add(node.right, k, v)
        elif k < node.k:
            node.left = self._add(node.left, k, v)
        else:  # 这个时候就是已经存在k键的时候
            node.v = v
        return node

    def _get(self, node, k):
        '''
        查找以node为根节点的map中键为k的节点的v
        若k不存在则返回None
        '''
        node = self._getNode(node, k)
        return node if node is not None else None

    def _set(self, node, k, v):
        '''
        将以node为根节点的map中携带键k的节点的v更新成v
        若k不存在，则报错
        '''
        node = self._getNode(node, k)
        if node is not None:
            node.v = v
        else:
            raise Exception('No key:"{}" in current map'.format(k))

    def _remove(self, node, k):
        '''
        删除以node为根节点的map中携带键为k的节点
        返回删除节点后的新的根节点
        若k不存在，则什么也不做
        '''

        def minimum(node):
            '''
            找到以node为根节点的map中携带最小k的节点
            '''
            if node.left is None:
                return node
            return minimum(node.left)

        def removeMin(node):
            '''
            删除以node为根节点的map中携带最小k的节点
            返回删除最小节点后的新的根节点
            '''
            if node.left is None:
                right_node = node.right
                right_node.right = None
                self.size -= 1
                return right_node
            node.left = removeMin(node.left)
            return node

        if node is None:  # 没找到
            return

        if node.k < k:
            node.right = self._remove(node.right, k)
            return node
        elif k < node.k:
            node.left = self._remove(node.left, k)
            return node
        # 现在找到了，分三种情况
        else:
            if node.left is None:
                right_node = node.right
                node.right = None
                self.size -= 1
                return right_node
            elif node.right is None:
                left_node = node.left
                node.left = None
                self.size -= 1
                return left_node
            else:  # 左右子树都不为空
                successer = minimum(node.right)
                successer.right = removeMin(node.right)
                # self.size += 1
                successer.left = node.left
                # 也要注意上面两条语句的顺序是不能颠倒的
                # self.size -= 1
                return successer