# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 03:24pm


import unittest

from src.ds.priority_queue import PriorityQueue


class Test_PriorityQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = PriorityQueue()

    def test_all(self):
        elems = [7, 4, 2, -1, 8, 10, 3, 6]
        # enqueue
        for elem in elems:
            self.processer.enqueue(elem)
        self.processer.print()
        # getFront
        print(self.processer.getFront())
        # dequeue
        dequeue_list = []
        while not self.processer.isEmpty():
            dequeue_list.append(self.processer.dequeue())
        self.processer.print()
        print(dequeue_list)


if __name__ == '__main__':
    unittest.main()