# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-21 07:59pm


import unittest
from src.ds.trie import Trie


class Test_Trie(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = Trie()
        self.processer_re = Trie()

    def test_all(self):
        strings = ['你好', 'hello', '老八', '奥利给', '巨魔战将']

        # test processer
        for string in strings:
            self.processer.add(string)
        self.processer.print()
        # contains
        print(self.processer.contains('奥利给'))
        print(self.processer.contains('奥利'))
        # prefix
        print(self.processer.is_prefix('奥利'))

        print('-------------- 华丽的分割线 --------------')

        # test processer_re
        for string in strings:
            self.processer_re.add_re(string)
        self.processer_re.print()
        print(self.processer_re.contains_re('奥利给'))
        print(self.processer_re.contains_re('奥利'))
        print(self.processer_re.is_prefix_re('奥利'))


if __name__ == '__main__':
    unittest.main()