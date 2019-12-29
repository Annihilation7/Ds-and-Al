# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-23 09:33pm


'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        回溯：dfs + 状态重置
        '''
        if len(nums) == 0:
            return []

        path = []
        res = []
        used = [False for _ in range(len(nums))]

        self._dfs(0, nums, path, res, used)

        return res

    def _dfs(self, index, nums, path, res, used):
        if index == len(nums):
            res.append(path.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self._dfs(index + 1, nums, path, res, used)

                used[i] = False
                path.pop()



if __name__ == '__main__':
    test = Solution()
    test_case = [1, 2, 3]
    print(test.permute(test_case))