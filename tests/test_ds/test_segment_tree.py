# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-21 05:40pm


import unittest
from src.ds.segment_tree import SegmentTree


class Test_SegmentTree(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [-2, 0, 3, -5, 2, -1]
        self.merger = lambda x, y: x + y  # 赋予线段树求区间和的功能
        self.processer = SegmentTree(self.data, self.merger)

    def test_all(self):
        # print
        self.processer.print()
        # query
        print(self.processer.query(0, 2))
        print(self.processer.query(2, 5))
        print(self.processer.query(0, 5))
        # set
        self.processer.set(1, 10)
        self.processer.print()
        # query
        print(self.processer.query(0, 2))
        print(self.processer.query(2, 5))
        print(self.processer.query(0, 5))


if __name__ == '__main__':
    unittest.main()