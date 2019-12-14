# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 11:47am


'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        一道dfs
        '''
        self.res = []
        self._dfs('', n, n)
        return self.res

    def _dfs(self, cur_str, left_num, right_num):
        if left_num == 0 and right_num == 0:
            self.res.append(cur_str)

        # 左括号只受自己的剩余数量的限制，无其他限制
        if left_num > 0:
            self._dfs(cur_str + '(', left_num - 1, right_num)
        # 右括号除了自己剩余数量的限制，为了保证括号的有效性，
        # 还受左括号剩余数量的限制，此时右括号的数量必须严格大于左括号的数量，才能
        # 向当前字符串中添加右括号
        if right_num > 0 and right_num > left_num:
            self._dfs(cur_str + ')', left_num, right_num - 1)