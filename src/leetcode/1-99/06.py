# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 11:45am


'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        遍历元素，同时维护一个长度为numRows的列表的列表，注意方向
        每次到numRows-1以及0的时候需要变换方向
        '''
        if numRows == 1:  # 1行需要特殊处理，否则res_index会越界
            return s
        res = ['' for _ in range(numRows)]
        direction = -1  # 第一次初始化为-1是因为要直接进入判断条件，所以会反过来的
        res_index = 0

        for elem in s:
            res[res_index] += elem
            direction = -direction \
                if res_index == 0 or res_index == numRows - 1 \
                else direction
            res_index += direction

        return ''.join(res)


if __name__ == '__main__':
    test = Solution()
    test_case = ['AB', 1]
    print(test.convert(*test_case))
