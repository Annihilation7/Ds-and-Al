# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-13 12:15am


'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        回溯算法（递归实现）
        '''
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']
            }
        res = []

        def add_letter(cur_string, num):
            if len(num) == 0:
                res.append(cur_string)
                return

            for elem in phone[num[0]]:
                add_letter(cur_string + elem, num[1: ])

        if len(digits):
            add_letter('', digits)

        return res


if __name__ == '__main__':
    test = Solution()
    test_case = '23'
    print(test.letterCombinations(test_case))
