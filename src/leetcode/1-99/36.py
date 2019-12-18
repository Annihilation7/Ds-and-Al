# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-18 09:48pm


'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


上图是一个部分填充的有效的数独。
数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

示例 2:
输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false

解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

说明:
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
'''


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        一次遍历比对 横、竖以及box上的条件
        '''

        rows = {}
        cols = {}
        boxs = {}

        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit == '.':
                    continue
                digit = int(digit)
                # 根据行id和列id确定box_id 非常关键
                box_id = row // 3 * 3 + col // 3
                row_flag = self._set_key(rows, row, digit)
                col_flag = self._set_key(cols, col, digit)
                box_flag = self._set_key(boxs, box_id, digit)
                if row_flag or col_flag or box_flag:
                    return False

        return True

    def _set_key(self, adict, key, num):
        if key in adict.keys():
            adict[key][num] += 1
            if adict[key][num] > 1:
                return True
        else:
            adict[key] = [0] * 10
            adict[key][num] = 1
        return False


if __name__ == '__main__':
    test = Solution()
    test_case = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(test.isValidSudoku(test_case))

