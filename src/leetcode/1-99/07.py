# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 12:11pm


'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution:
    def reverse(self, x: int) -> int:
        '''
        很简单，基本没啥东西，python也不存在越界问题，最后判断一下就好了
        '''
        res = 0
        pos_x = x if x >= 0 else -x

        while pos_x:
            tail_num = pos_x % 10
            res = res * 10 + tail_num
            pos_x //= 10

        res = res if x >= 0 else -res  # 注意符号位

        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0