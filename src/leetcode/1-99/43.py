# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-22 08:56pm


'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，
它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        模拟平行乘法操作，思路是比较简单的
        不过这个方法时间比较慢。。
        '''
        if num1 == '0' or num2 == '0':
            return '0'

        muls = self._multiply(num1, num2)
        res = ''.join(muls[0])
        for i in range(1, len(muls)):
            res = self._combine(res, muls[i])
        return res

    def _multiply(self, num1, num2):
        res = []
        for i in range(len(num2) - 1, -1, -1):
            tmp = []
            c = 0
            for j in range(len(num1) - 1, -1, -1):
                mul_i = int(num2[i])
                mul_j = int(num1[j])
                mul = mul_i * mul_j + c
                c = mul // 10
                tmp_res = str(mul % 10)
                tmp.append(tmp_res)
            if c != 0:
                tmp.append(str(c))
            tmp.reverse()
            # 补0
            for num in range(len(num2) - i - 1):
                tmp.append('0')
            res.append(tmp)
        return res

    def _combine(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        res = ''
        while i >= 0 or j >= 0:
            tmp1 = int(num1[i]) if i >= 0 else 0
            tmp2 = int(num2[j]) if j >= 0 else 0
            tmp_sum = tmp1 + tmp2 + c
            res += str(tmp_sum % 10)
            c = tmp_sum // 10

            i -= 1
            j -= 1
        if c != 0:
            res += str(c)

        return res[::-1]


if __name__ == '__main__':
    test = Solution()
    test_case = ['66', '99']
    print(test.multiply(*test_case))