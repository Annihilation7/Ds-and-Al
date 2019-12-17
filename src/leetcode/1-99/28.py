# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-16 09:17pm


'''
实现S strtr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 
以及 Java的 indexOf() 定义相符。
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        高大上的kmp算法咱也不会，最终还是暴力方法做的- -
        '''
        if len(needle) == 0:
            return 0

        outer_index = 0

        while outer_index < len(haystack):
            if haystack[outer_index] == needle[0]:
                # 找到第一个一样的时候，haystack的剩余长度已经小于needle了，匹配是
                # 一定失败的
                if len(haystack) - outer_index < len(needle):
                    return -1
                inter_index = 0
                while inter_index < len(needle) and \
                        haystack[outer_index + inter_index] == needle[inter_index]:
                    inter_index += 1
                if inter_index == len(needle):
                    return outer_index
            outer_index += 1

        return -1