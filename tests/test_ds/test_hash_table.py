# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-07 05:11pm


import unittest
from src.ds.hash_table import HashTable
import random
import string


class Test_HashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = HashTable()
        self.test_size = 1000  # hash_table的大小
        self.elems = [
            (i, random.choice(string.ascii_lowercase))
            for i in range(self.test_size)
        ]

    def test_all(self):
        for elem in self.elems:
            self.processer.add(*elem)
        self.processer.print()
        self.processer.remove(8)
        self.processer.print()
        self.processer.set(6, '奥力给')
        self.processer.print()
        print(self.processer.contains(6))
        print(self.processer.get(6))


if __name__ == '__main__':
    unittest.main()