# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-01-23 01:27pm


import unittest
from src.ds.avl_set import AvlSet


class Test_SetAvl(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = AvlSet()

    def test_all(self):
        elems = [5, 3, 6, 8, 4, 2]
        # add
        for elem in elems:
            self.processer.add(elem)
        self.processer.print()
        print()
        # remove
        self.processer.remove(3)
        self.processer.print()
        print()
        # contains
        print(self.processer.contains(4))
        # getSize
        print(self.processer.getSize())


if __name__ == '__main__':
    unittest.main()

