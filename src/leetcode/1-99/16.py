# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-13 12:06am


'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        和上一题的思路是差不多的
        '''
        appro = float('inf')

        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tmp_res = nums[i] + nums[left] + nums[right]
                if tmp_res == target:
                    return target
                appro = appro \
                    if abs(appro - target) < abs(tmp_res - target) else tmp_res
                if tmp_res > target:
                    right -= 1
                else:
                    left += 1

        return appro