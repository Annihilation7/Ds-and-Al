# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-01-23 01:29pm


import unittest
from src.ds.avl_map import AvlMap


class Test_AvlMap(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = AvlMap()

    def test_all(self):
        elems = [(5, 'e'), (3, 'c'), (6, 'b'), (8, 'f'), (4, 'd'), (2, 'a')]
        # add
        for elem in elems:
            self.processer.add(*elem)
        self.processer.add(6, 'gengxin')
        self.processer.print()
        # contains
        print(self.processer.contains(3))
        # get
        print(self.processer.get(6))
        # set
        self.processer.set(6, 'caibi')
        self.processer.print()
        # remove
        self.processer.remove(6)
        self.processer.print()
        # check
        print('is bst? {}'.format(self.processer.isBst()))
        print('is balanced? {}'.format(self.processer.isBalanced()))
        # total keys-values
        print('total keys-values: {}'.format(AvlMap().items()))


if __name__ == '__main__':
    unittest.main()