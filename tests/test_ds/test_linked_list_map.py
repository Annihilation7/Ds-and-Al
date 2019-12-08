# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-07 1:11pm


import unittest
from src.ds.linked_list_map import LinkedListMap


class Test_LinkedListMap(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = LinkedListMap()

    def test_all(self):
        elems = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

        # add
        for elem in elems:
            self.processer.add(*elem)
        self.processer.print()
        # get
        print(self.processer.get('c'))
        # set
        self.processer.set('d', 'caibi')
        self.processer.print()
        # remove
        self.processer.remove('d')
        self.processer.print()


if __name__ == '__main__':
    unittest.main()