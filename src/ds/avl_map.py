# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-01-22 09:32pm


from src.ds.loop_queue import LoopQueue


class Node:
    def __init__(self, k=None, v=None, left=None, right=None):
        self.k = k
        self.v = v
        self.left = left
        self.right = right
        self.height = 1


class AvlMap:
    def __init__(self):
        """Avl树认为的平衡状态是对于任意一个Node，它的左子树与右子树的高度差不超过1"""
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def isBst(self):
        """
        用于验证的辅助函数1，判断当前树是否是一颗二分搜索树。
        运用中序遍历的性质来做
        """
        def isBst_node(node):
            value_records = []
            inorder(node, value_records)

            if len(value_records) == 0:  # self.root=None也认为是二分搜树
                return True

            for i in range(1, len(value_records)):
                if value_records[i - 1] > value_records[i]:
                    return False
            return True

        def inorder(node, value_records):
            if node is None:
                return
            inorder(node.left, value_records)
            value_records.append(node.k)
            inorder(node.right, value_records)

        return isBst_node(self.root)

    def isBalanced(self):
        """用于验证的辅助函数2，判断当前树是否是一颗平衡二叉树。遍历就完事了"""
        def isBalanced_node(node):
            if node is None:
                return True  # 遍历到None还没有触发False语句，那么该支路就是平衡的
            balance = self._get_balance(node)
            if abs(balance) >= 2:
                return False
            return isBalanced_node(node.left) and isBalanced_node(node.right)

        return isBalanced_node(self.root)

    def get(self, k):
        ret_node = self._get_node(self.root, k)
        return ret_node.v if ret_node is not None else None

    def set(self, k, v):
        node = self._get_node(self.root, k)
        if node is None:
            raise Exception('key:{} is not in avl map.'.format(k))
        node.v = v

    def add(self, k, v):
        self.root = self._add(self.root, k, v)

    def contains(self, k):
        return self._contains(self.root, k)

    def print(self):
        if self.isEmpty():
            print('Empty avl map')
            return
        self._print(self.root)
        print()

    def remove(self, elem):
        '''删除bst中key=elem的节点，并返回其value值。不存在的话返回None'''
        assert not self.isEmpty(), 'empty avl map'
        ret_node = self.get(elem)
        if ret_node is not None:
            self.root = self._remove(self.root, elem)
        return ret_node

    def items(self):
        """
        返回当前avl树中所有(key, value)的列表，采用前序遍历的方法来做
        该函数的主要作用是用在了hash table的扩容/所容过程中的元素复制
        """
        def _items(node):
            nonlocal total_keys
            if node is None:
                return
            total_keys.append((node.k, node.v))
            _items(node.left)
            _items(node.right)

        total_keys = []
        _items(self.root)
        return total_keys

    # private
    def _to_balanced(self, y):
        """
        AVL树核心函数，以y为根的二分搜索树已经不平衡，根据相应的不平衡情况做出
        适当的旋转操作
        """

        def ll(y):
            """
            case1 左-左（LL） -> 右旋转

                      y                              x
                    /   \                          /    \
                   x     T4                       z      y
                  / \                ->         /  \    / \
                 z   T3                       T1   T2  T3  T4
                /  \
               T1   T2
            """
            x = y.left
            T3 = x.right

            x.right = y
            y.left = T3

            # 注意先y后x
            y.height = \
                1 + max(self._get_height(y.left), self._get_height(y.right))
            x.height = \
                1 + max(self._get_height(x.left), self._get_height(x.right))

            # 返回新的根节点x
            return x

        def rr(y):
            """
            case2 右-右（RR） -> 左旋转

                    y                                      x
                  /   \                                  /    \
                 T4    x                                y       z
                     /   \                 ->          /  \    /  \
                    T3    z                           T4   T3 T2  T1
                         /  \
                        T2   T1
            """
            x = y.right
            T3 = x.left

            x.left = y
            y.right = T3

            y.height = \
                1 + max(self._get_height(y.left), self._get_height(y.right))
            x.height = \
                1 + max(self._get_height(x.left), self._get_height(x.right))

            return x

        if abs(self._get_balance(y)) <= 1:
            return y

        # 把子节点 = 的情况归为ll和rr了，也可以归为lr和rl，一样的
        if self._get_balance(y) >= 2 and self._get_balance(y.left) >= 0:
            return ll(y)
        elif self._get_balance(y) <= -2 and self._get_balance(y.right) <= 0:
            return rr(y)
        elif self._get_balance(y) >= 2 and self._get_balance(y.left) < 0:
            """
            case3 左->右（lr） -> 先rr其左节点，再ll
                    y                      y
                  /  \                    /  \
                 x    T4        ->       z    T4    ->   ll
                / \                     / \
               T1  z                   x   T3
                 /  \                 / \
                T2   T3              T1  T2
            """
            y.left = rr(y.left)
            return ll(y)
        elif self._get_balance(y) <= -2 and self._get_balance(y.right) > 0:
            """
            case4 右->左(rl)  -> 先ll其右节点，再rr
                    y                          y
                   / \                        /  \
                  T1  x                      T1   z
                     /  \         ->             /  \          ->   rr
                    z    T4                     T2   x 
                   /  \                             /  \
                  T2  T3                           T3   T4  
            """
            y.right = ll(y.right)
            return rr(y)

    def _get_height(self, node):
        """获取一个Node的高度，该Node有可能为None"""
        return node.height if node is not None else 0

    def _get_balance(self, node):
        """获取一个Node的平衡因子，该Node有可能为None。另外这里是左减右"""
        if node is None:
            return 0  # None必平衡，所以平衡因子为0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_node(self, node, k):
        if node is None:
            return None

        if node.k < k:
            return self._get_node(node.right, k)
        if k < node.k:
            return self._get_node(node.left, k)
        # equal
        return node

    def _add(self, node, k, v):
        if node is None:
            self.size += 1
            return Node(k, v)

        if node.k < k:
            node.right = self._add(node.right, k, v)
        elif k < node.k:
            node.left = self._add(node.left, k, v)

        # 回溯的时候更新height，后面可能会触发to_balance操作
        node.height = 1 + max(
            self._get_height(node.left), self._get_height(node.right)
        )  # 这里的node肯定不是None，所以可以放心调用

        return self._to_balanced(node)

    def _contains(self, node, k):
        if node is None:
            return False

        if node.k == k:
            return True
        elif node.k < k:
            return self._contains(node.right, k)
        else:
            return self._contains(node.left, k)

    def _print(self, node):
        queue = LoopQueue()
        queue.enqueue(node)

        while not queue.isEmpty():
            dequeue_node = queue.dequeue()
            print(
                '(key:{}->value:{})'.format(dequeue_node.k, dequeue_node.v),
                end=', '
            )
            if dequeue_node.left is not None:
                queue.enqueue(dequeue_node.left)
            if dequeue_node.right is not None:
                queue.enqueue(dequeue_node.right)

    def _minimum(self, node):
        if node.left is None:
            return node
        return self._minimum(node.left)

    def _removeMin(self, node):
        ret_node = None
        if node.left is None:
            right_node = node.right
            node.right = None
            self.size -= 1
            ret_node = right_node

        elif node.left is not None:
            node.left = self._removeMin(node.left)
            ret_node = node

        if ret_node is not None:
            ret_node.height = \
                1 + max(
                    self._get_height(ret_node.left),
                    self._get_height(ret_node.right)
                )
        return self._to_balanced(ret_node)

    def _remove(self, node, k):
        if node is None:  # 没找到携带键k的节点。。
            return None

        # 三种情况：大于，小于，等于
        ret_node = None
        if node.k < k:
            node.right = self._remove(node.right, k)
            ret_node = node
        elif k < node.k:
            node.left = self._remove(node.left, k)
            ret_node = node
        else:
            # 此时处理相等的情况
            if node.left is None:  # 只有右子树
                right_node = node.right
                node.right = None
                self.size -= 1
                ret_node = right_node
            elif node.right is None:  # 只有左子树
                left_node = node.left
                node.left = None
                self.size -= 1
                ret_node = left_node
            else:  # 左、右子树均不为None，这里用"后继（右子树中的最小值）"节点来实现
                successer = self._minimum(node.right)
                successer.right = self._removeMin(node.right)
                successer.left = node.left
                # self.size += 1  # 这个时候还没有真正的删除
                # 上面的right与left语句绝不能颠倒！！画个图一看就知道了！
                node.left = node.right = None
                # self.size -= 1
                ret_node = successer

        # keep balance
        if ret_node is not None:
            ret_node.height = \
                1 + max(
                    self._get_height(ret_node.left),
                    self._get_height(ret_node.right)
                )
        return self._to_balanced(ret_node)