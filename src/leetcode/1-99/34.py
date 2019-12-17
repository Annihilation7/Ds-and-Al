# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-17 10:45pm


'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        二分模版法
        两次查找，分别对应左中位数和右中位数，最终的查找结果就是左边界和右边界
        '''
        if len(nums) == 0:
            return [-1, -1]

        res = []

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            res.append(left)
        else:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] == target:
            res.append(right)

        return res



