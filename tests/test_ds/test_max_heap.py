# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 02:27am


import unittest

from src.ds.max_heap import MaxHeap


class Test_MaxHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = MaxHeap()

    def test_all(self):
        elems = [3, 5, 7, 2, 1]
        # add
        for elem in elems:
            self.processer.add(elem)
        self.processer.print()
        # findmax
        print(self.processer.find_max())
        # extractMax
        max_num = self.processer.extractMax()
        print(max_num)
        self.processer.print()
        # replace
        ret = self.processer.replace(-1)
        print(ret)
        self.processer.print()
        # heapify
        alist = [3, 5, 7, 2, 1]
        self.processer.heapify(alist)
        self.processer.print()


if __name__ == '__main__':
    unittest.main()

