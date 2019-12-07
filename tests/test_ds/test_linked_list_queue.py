# -*- coding: utf-8 -*-
# Email: mazhenyu@datagrand.com
# Created: 2019-12-07 12:57pm


import unittest
from src.ds.linked_list_queue import LinkedListQueue


class Test_LinkedListQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = LinkedListQueue()

    def test_all(self):
        elems = [i for i in range(20)]
        # enqueue
        for elem in elems:
            self.processer.enqueue(elem)
        self.processer.print()
        # dequeue, to empty
        for i in range(20):
            self.processer.dequeue()
        self.processer.print()
        # enqueue
        for elem in elems:
            self.processer.enqueue(elem)
        self.processer.print()


if __name__ == '__main__':
    unittest.main()