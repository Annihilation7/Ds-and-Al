# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-10 1:14pm


'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
'''


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        所有的公共前缀和两两前缀一直比到最后一个元素是等价的
        '''
        if len(strs) == 0:
            return ''

        res = strs[0]
        i = 1

        while i < len(strs):
            tmp_res = self._get_prefix(res, strs[i])
            if tmp_res == '':
                return ''
            res = res if len(res) < len(tmp_res) else tmp_res
            i += 1

        return res

    def _get_prefix(self, str1, str2):
        res = ''

        length = min(len(str1), len(str2))
        for i in range(length):
            if str1[i] == str2[i]:
                res += str1[i]
            else:
                break

        return res


if __name__ == '__main__':
    test = Solution()
    test_case = ["flower","flow","flight"]
    print(test.longestCommonPrefix(test_case))