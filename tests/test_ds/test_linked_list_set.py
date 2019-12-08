# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 12:44pm


import unittest
from src.ds.linked_list_set import LinkedListSet


class Test_SetBst(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = LinkedListSet()

    def test_all(self):
        elems = [5, 3, 6, 8, 4, 2]
        # add
        for elem in elems:
            self.processer.add(elem)
        self.processer.print()
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
