# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 01:42am


'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        栈的简单应用，非常的基础
        '''
        left_set = ['(', '{', '[']
        right_set = [')', '}', ']']
        stack = []

        for elem in s:
            if elem in left_set:
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                if left_set.index(stack[-1]) != right_set.index(elem):
                    return False
                stack.pop()

        return True if len(stack) == 0 else False