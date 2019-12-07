# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-07 01:51pm


from src.ds.bst import BST
import unittest


class Test_BST(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = BST()

    def test_all(self):
        elems = [5, 3, 6, 8, 4, 2]

        # add
        for elem in elems:
            self.processer.add(elem)
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


if __name__ == '__main__':
    unittest.main()
