# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-16 09:33pm


'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2

说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，
如果除法结果溢出，则返回 231 − 1。
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        两个核心思路：
            - 减法
            - 通过位运算倍增除数以减少实际的运算次数，防止超时
        '''
        res = 0
        sign = 1 if dividend ^ divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            divisor_cp = divisor
            ratio = 1
            while dividend >= divisor_cp:
                dividend -= divisor_cp
                res += ratio
                ratio <<= 1
                divisor_cp <<= 1

        res *= sign
        return min(max(res, -2 ** 31), 2 ** 31 - 1)


if __name__ == '__main__':
    test = Solution()
    test_case = [12, -3]
    print(test.divide(*test_case))