# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-18 11:02m


'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n - 1):
            tmp_res = ''
            index = 0
            while index < len(res):
                next_index = index + 1
                count = 1
                while next_index < len(res) and res[next_index] == res[index]:
                    count += 1
                    next_index += 1
                tmp_res += (str(count) + res[index])
                index = next_index
            res = tmp_res
        return res


if __name__ == '__main__':
    test = Solution()
    test_case = 4
    print(test.countAndSay(test_case))