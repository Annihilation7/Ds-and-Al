# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-01-22 09:32pm


from src.ds.avl_tree import AvlTree
import unittest


class Test_AVL(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = AvlTree()

    def test_all(self):
        elems = [i for i in range(100)]

        # add
        for elem in elems:
            self.processer.add(elem)  # bst此时会退化成链表
        # contains
        print(self.processer.contains(6))
        # preorder
        self.processer.preOrder()
        # preorderNR
        print()
        self.processer.preOrderNR()
        print()
        # inorder
        self.processer.inOrder()
        print()
        # postorder
        self.processer.postOrder()
        print()
        # levelorder
        self.processer.levelOrder()
        print()
        # minimum
        print(self.processer.minimum())
        # maximum
        print(self.processer.maximum())
        # removeMin
        self.processer.removeMin()
        self.processer.levelOrder()
        print()
        # removeMax
        self.processer.removeMax()
        self.processer.levelOrder()
        print()
        print(self.processer.getSize())
        # remove
        self.processer.remove(6)
        self.processer.levelOrder()
        print()
        print(self.processer.getSize())

        print('is bst? {}'.format(self.processer.isBst()))
        print('is balanced? {}'.format(self.processer.isBalanced()))


if __name__ == '__main__':
    unittest.main()