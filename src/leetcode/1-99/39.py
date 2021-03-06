# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-18 11:32m


'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        if len(candidates) == 0:
            return []

        candidates.sort()

        self._dfs(candidates, 0, path, res, target)

        return res

    def _dfs(self, candidates, begin_index, path, res, target):
        if target == 0:
            res.append(path[:])
            return

        for i in range(begin_index, len(candidates)):
            residual = target - candidates[i]
            if residual < 0:
                break
            path.append(candidates[i])
            self._dfs(candidates, i, path, res, residual)

            path.pop()