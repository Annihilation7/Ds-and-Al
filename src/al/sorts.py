# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-01-26 12:03am


import random


class SortsFactory:

    @classmethod
    def bubble_sort(cls, alist):
        """
            冒泡排序 —— O(N ^ 2)
        """
        # 不用到0，因为倒数第二次换完最后一个一定是最小的了
        for i in range(len(alist) - 1, 0, -1):
            for j in range(1, i + 1):
                if alist[j] < alist[j - 1]:
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]

    @classmethod
    def selection_sort(cls, alist):
        """
            选择排序 —— O(N ^ 2)
        """
        for i in range(len(alist)):
            min_index = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[min_index]:
                    min_index = j
            alist[i], alist[min_index] = alist[min_index], alist[i]

    @classmethod
    def insertion_sort(cls, alist):
        """
            插入排序 —— O(N ^ 2)
            近乎有序的数组中排序的速度会很快
        """
        for i in range(1, len(alist)):
            e = alist[i]
            j = i
            while j > 0 and alist[j - 1] > e:
                alist[j] = alist[j - 1]
                j -= 1
            alist[j] = e

    @classmethod
    def merge_sort_ud(cls, alist):
        """
            自顶向下归并排序 —— O(N ^ logN)，需要额外的O(N)的空间复杂度
            小数据量下加两条优化条件反而变慢了。。
        """
        def _merge_sort(alist, l, r):
            """左闭右闭区间"""
            if r - l >= 15:  # 优化1，小数据量下改为直接进行插入排序处理
                SortsFactory._insertion_sort(alist, l, r)
                return

            mid = l + (r - l) // 2
            _merge_sort(alist, l, mid)
            _merge_sort(alist, mid + 1, r)
            # 优化2  注意回溯过程中数组本身就是有序的，所以这个条件有时可以让回溯
            # 变得更快
            if alist[mid] > alist[mid + 1]:
                SortsFactory._merge(alist, l, mid, r)

        _merge_sort(alist, 0, len(alist) - 1)

    @classmethod
    def merge_sort_du(cls, alist):
        """
            自底向上归并排序 —— O(N ^ logN)，需要额外的O(N)的空间复杂度
        """
        sz = 1
        while sz <= len(alist):
            i = 0
            while i + sz < len(alist):
                SortsFactory._merge(
                    alist, i, i + sz - 1, min(i + 2 * sz - 1, len(alist) - 1)
                )
                i += 2 * sz
            sz += sz

    @classmethod
    def quick_sort(cls, alist):
        """
            快速排序 —— O(N * logN)
            三路快排，针对近乎有序的数组也有非常好的性能，牛逼就完事了
        """
        def _quick_sort(alist, l, r):
            """左闭右闭区间"""
            if r - l <= 15:
                SortsFactory._insertion_sort(alist, l, r)
                return

            random_index = random.randint(l, r)
            alist[l], alist[random_index] = alist[random_index], alist[l]

            lt = l  # [l, lt]  <
            gt = r + 1  # [gt, r]  >
            i = l + 1  # [lt + 1, i)  ==

            while i < gt:  # 一定要理解好循环不变量的意义
                if alist[i] < alist[l]:
                    alist[lt + 1], alist[i] = alist[i], alist[lt + 1]
                    lt += 1
                    i += 1
                elif alist[l] < alist[i]:
                    alist[gt - 1], alist[i] = alist[i], alist[gt - 1]
                    gt -= 1
                else:
                    i += 1

            alist[l], alist[lt] = alist[lt], alist[l]
            _quick_sort(alist, l, lt - 1)  # 体会一下为什么是lt-1，很简单
            _quick_sort(alist, gt, r)

        _quick_sort(alist, 0, len(alist) - 1)

    @classmethod
    def heap_sort(cls, alist):
        """
            堆排序（基于最大堆） —— O(N * logN)
        """
        def _shiftdown(alist, n, i):
            """将索引i在alist的前n个数中进行shiftdown操作，这里起始索引设为0"""
            while 2 * i + 1 < n:
                j = 2 * i + 1
                if j + 1 < n and alist[j + 1] > alist[j]:
                    j += 1
                if alist[i] >= alist[j]:
                    break
                alist[i], alist[j] = alist[j], alist[i]
                i = j

        # heapify stage
        for i in range((len(alist) - 1 - 1) // 2, -1, -1):
            _shiftdown(alist, len(alist), i)
        # heap sort
        for i in range(len(alist) - 1, 0, -1):
            alist[0], alist[i] = alist[i], alist[0]
            _shiftdown(alist, i, 0)

    @staticmethod
    def _merge(alist, l, mid, r):
        """merge独立出来的原因是自底向上和自顶向下的mergesort都会用到_merge函数"""
        aux = [elem for elem in alist[l: r + 1]]
        i = l
        j = mid + 1

        for k in range(l, r + 1):
            if i > mid:
                alist[k] = aux[j - l]
                j += 1
                continue
            if j > r:
                alist[k] = aux[i - l]
                i += 1
                continue
            if aux[i - l] < aux[j - l]:
                alist[k] = aux[i - l]
                i += 1
            else:
                alist[k] = aux[j - l]
                j += 1

    @staticmethod
    def _insertion_sort(alist, l, r):
        """
        区间上的insertion_sort独立出来的原因是merge_sort_ud和快排都能用到
        左闭右闭区间
        """
        for i in range(l + 1, r + 1):
            e = alist[i]
            j = i
            while j > l and alist[j - 1] > e:
                alist[j] = alist[j - 1]
                j -= 1
            alist[j] = e