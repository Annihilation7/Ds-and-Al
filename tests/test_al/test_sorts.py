# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-01-26 12:14am


import functools
import random
import time
import unittest

from src.al.sorts import SortsFactory


def time_wrapper(func):
    @functools.wraps(func)
    def count_time(*args, **kwargs):
        st = time.time()
        ret = func(*args, **kwargs)
        print('"{}" function time cost: {:.4f}s'.format(
            func.__name__, time.time() - st
        ))
        return ret
    return count_time


class Test_SortsFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.test_case = self._generate_random_list()

    @time_wrapper
    def test_bubble_sort(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.bubble_sort(test_case)
        assert self._check(test_case) == True

    @time_wrapper
    def test_selection_sort(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.selection_sort(test_case)
        assert self._check(test_case) == True

    @time_wrapper
    def test_insertion_sort(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.insertion_sort(test_case)
        assert self._check(test_case) == True

    @time_wrapper
    def test_merge_sort_ud(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.merge_sort_ud(test_case)
        assert self._check(test_case) == True

    @time_wrapper
    def test_merge_sort_du(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.merge_sort_du(test_case)
        assert self._check(test_case) == True

    @time_wrapper
    def test_quick_sort(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.quick_sort(test_case)
        assert self._check(test_case) == True

    @time_wrapper
    def test_heap_sort(self):
        test_case = self._copy_case(self.test_case)
        SortsFactory.heap_sort(test_case)
        assert self._check(test_case) == True

    def _generate_random_list(self):
        return [random.randint(0, 10000) for _ in range(5000)]

    def _check(self, sorted_list):
        for i in range(1, len(sorted_list)):
            if sorted_list[i] < sorted_list[i - 1]:
                return False
        return True

    def _copy_case(self, test_case):
        return test_case.copy()


if __name__ == '__main__':
    unittest.main()
