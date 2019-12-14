# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
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


if __name__ == '__main__':
    unittest.main()

