# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-07 01:51pm


from src.ds.array_queue import ArrayQueue
from src.ds.array_stack import ArrayStack


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, elem):
        '''向bst中添加元素elem'''
        self.root = self._add(self.root, elem)

    def contains(self, elem):
        '''查询bst中是否包含元素elem'''
        return self._contains(self.root, elem)

    def preOrder(self):
        '''bst的前序遍历'''
        if self.size == 0:
            print('empty bst')
            return
        self._preOrder(self.root)

    def preOrderNR(self):
        '''bst前序遍历的非递归写法，需要借助栈'''
        if self.size == 0:
            print('empty bst')
            return
        stack = ArrayStack()
        stack.push(self.root)
        while not stack.isEmpty():
            node = stack.pop()
            print(node.data, end=', ')
            if node.right is not None:  # 先右孩子，后左孩子
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)

    def inOrder(self):
        '''bst的中序遍历'''
        if self.size == 0:
            print('empty bst')
            return
        self._inOrder(self.root)

    def postOrder(self):
        '''bst的后序遍历'''
        if self.size == 0:
            print('empty bst')
            return
        self._postOrder(self.root)

    def levelOrder(self):
        '''bst的广度优先遍历'''
        if self.size == 0:
            print('empty bst')
            return
        queue = ArrayQueue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            node = queue.dequeue()
            print(node.data, end=', ')
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def minimum(self):
        '''返回bst中的最小值'''
        assert not self.isEmpty(), 'empty bst'
        return self._minimum(self.root).data

    def maximum(self):
        '''返回bst中的最大值'''
        assert not self.isEmpty(), 'empty bst'
        return self._maximum(self.root).data

    def removeMin(self):
        '''删除bst中携带最小值的节点，并返回它所携带的元素的值'''
        ret = self.minimum()  # 已经做合法性检查了
        self.root = self._removeMin(self.root)
        return ret

    def removeMax(self):
        '''删除bst中携带最大值的节点，并返回它所携带的元素的值'''
        ret = self.maximum()
        self.root = self._removeMax(self.root)
        return ret

    def remove(self, elem):
        '''删除bst中携带元素elem的节点'''
        assert not self.isEmpty(), 'empty bst'
        self.root = self._remove(self.root, elem)

    # private
    def _add(self, node, elem):
        '''
        向以node为根节点的bst中的插入元素elem
        返回插入元素后新的根节点
        '''
        if node is None:
            self.size += 1
            return Node(elem)

        if node.data < elem:
            node.right = self._add(node.right, elem)
        elif elem < node.data:
            node.left = self._add(node.left, elem)
        # 所以上面的逻辑代表了bst中不包含重复元素
        return node  # 逐级往上返回，直到根节点

    def _contains(self, node, elem):
        '''
        查询以node为根节点的bst中是否包含elem
        '''
        if node is None:
            return False

        if node.data == elem:
            return True
        elif node.data < elem:
            return self._contains(node.right, elem)
        else:
            return self._contains(node.left, elem)

    def _preOrder(self, node):
        '''对以node为根节点的bst进行前序遍历'''
        if node is None:
            return

        print(node.data, end=', ')
        self._preOrder(node.left)
        self._preOrder(node.right)

    def _inOrder(self, node):
        '''对以node为根节点的bst进行中序遍历'''
        if node is None:
            return

        self._inOrder(node.left)
        print(node.data, end=', ')
        self._inOrder(node.right)

    def _postOrder(self, node):
        '''对以node为跟节点的bst进行后序遍历'''
        if node is None:
            return

        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.data, end=', ')

    def _minimum(self, node):
        '''找到以node为根节点的bst中携带最小值的节点'''
        if node.left is None:
            return node
        return self._minimum(node.left)

    def _maximum(self, node):
        '''找到以node为根节点的bst中携带最大值的节点'''
        if node.right is None:
            return node
        return self._maximum(node.right)

    def _removeMin(self, node):
        '''删除携带最小值的节点，返回删除后的bst的根节点'''
        if node.left is None:
            right_node = node.right
            node.right = None
            self.size -= 1
            return right_node

        if node.left is not None:
            node.left = self._removeMin(node.left)
        return node

    def _removeMax(self, node):
        '''删除携带最大值的节点，返回删除后的bst的跟节点'''
        if node.right is None:
            left_node = node.left
            node.left = None
            self.size -= 1
            return left_node

        if node.right is not None:
            node.right = self._removeMax(node.right)
        return node

    def _remove(self, node, elem):
        '''
        删除以node为跟节点的bst中携带元素elem的节点
        返回删除节点后的新的根节点
        '''
        if node is None:  # 没找到携带elem的节点。。
            return
        # 三种情况：大于，小于，等于
        if node.data < elem:
            node.right = self._remove(node.right, elem)
            return node
        if elem < node.data:
            node.left = self._remove(node.left, elem)
            return node
        # 此时处理相等的情况
        if node.left is None:  # 只有右子树
            right_node = node.right
            node.right = None
            self.size -= 1
            return right_node
        elif node.right is None:  # 只有左子树
            left_node = node.left
            node.left = None
            self.size -= 1
            return left_node
        else:  # 左、右子树均不为None，这里用"后继（右子树中的最小值）"节点来实现
            successer = self._minimum(node.right)
            successer.right = self._removeMin(node.right)
            successer.left = node.left
            # self.size += 1  # 这个时候还没有真正的删除
            # 上面的right与left语句绝不能颠倒！！画个图一看就知道了！
            node.left = node.right = None
            # self.size -= 1
            return successer  # 将后继返回
