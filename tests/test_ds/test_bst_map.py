# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-07 02:03pm


import unittest
from src.ds.bst_map import BstMap


class Test_LinkedListMap(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = BstMap()

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


if __name__ == '__main__':
    unittest.main()