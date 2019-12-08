# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 11:28am


'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        采用中心扩展算法来解决本题
        注意：注意中心有可能是一个，如bab。也有可能是两个，如baab
        '''
        res = ''

        for i in range(len(s)):
            center_1 = self._expand(s, i, i)
            center_2 = self._expand(s, i, i + 1)
            center = center_1 if len(center_1) > len(center_2) else center_2
            res = res if len(res) > len(center) else center

        return res

    def _expand(self, s, left_center, right_center):
        res = ''

        while left_center >= 0 and right_center < len(s) and \
                s[left_center] == s[right_center]:
            res = s[left_center: right_center + 1]
            left_center -= 1
            right_center += 1

        return res


if __name__ == '__main__':
    test = Solution()
    test_case = 'babad'

    print(test.longestPalindrome(test_case))
