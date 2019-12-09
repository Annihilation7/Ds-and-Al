# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-09 12:11am


'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        负数直接先pass
        用类似头尾双指针的方法来做这道题
        '''
        if x < 0:
            return False

        k = 1
        while x // k >= 10:
            k *= 10

        while x:
            left = x // k
            right = x % 10

            if left != right:
                return False

            # 最关键的两步
            # 一个是如何求除了左右两数字之外剩下的数
            # 一个是k应该怎么变化
            # 举个小例子看一下就好了，不难
            x = x % k // 10
            k //= 100

        return True


