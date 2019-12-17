# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-17 11:01pm


'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
'''


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        神奇的二分查找算法
        '''
        if target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
