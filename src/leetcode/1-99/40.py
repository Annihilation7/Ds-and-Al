# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-22 08:31m


'''
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        candidates.sort()

        self._dfs(candidates, 0, path, res, target)

        return res

    def _dfs(self, candidates, begin_index, path, res, target):
        if target == 0:
            res.append(path[:])
            return

        for i in range(begin_index, len(candidates)):
            if i > begin_index and candidates[i] == candidates[i - 1]:
                continue
            residual = target - candidates[i]
            if residual < 0:
                break
            path.append(candidates[i])
            self._dfs(candidates, i + 1, path, res, residual)
            path.pop()


if __name__ == '__main__':
    test = Solution()
    test_case = {
        'candidates': [10, 1, 2, 7, 6, 1, 5],
        'target': 8
    }
    print(test.combinationSum2(**test_case))