# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-07 03:41am


import unittest

from src.ds.rb_tree import RbTree


class Test_RbTree(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = RbTree()
        self.elems = [5, 3, 6, 8, 4, 2]

    def test_all(self):
        for elem in self.elems:
            self.processer.add(elem)
        self.processer.print()


if __name__ == '__main__':
    unittest.main()