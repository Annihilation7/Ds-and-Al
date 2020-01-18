# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-21 07:59pm


import random
import time
import unittest

from src.ds.union_find import *


class Test_UnionFind(unittest.TestCase):
    def setUp(self) -> None:
        self.size = 10000
        self.op_nums = 10000
        self.unionfinds = [
            UnionFind1(self.size),
            UnionFind2(self.size),
            UnionFind3(self.size),
            UnionFind4(self.size),
            UnionFind5(self.size),
            UnionFind6(self.size)
        ]

    def test_all(self):
        for uf in self.unionfinds:
            self._calc_time(uf, self.size)

    def _calc_time(self, uf, op_nums):
        st = time.time()
        for i in range(op_nums):
            p = random.randint(0, uf.getSize() - 1)  # 左闭右闭
            q = random.randint(0, uf.getSize() - 1)
            uf.isConnected(p, q)
        for i in range(op_nums):
            p = random.randint(0, uf.getSize() - 1)
            q = random.randint(0, uf.getSize() - 1)
            uf.union(p, q)
        print(
            '{} totally time cost: {:.4f}s'.format(uf, time.time() - st)
        )


if __name__ == '__main__':
    unittest.main()
