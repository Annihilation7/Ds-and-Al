# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-11 11:48pm


'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        先排序，然后遍历每个元素求合适的三元组，注意滤重就可以了
        '''
        res = []

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:  # 此时不用想了，后面肯定没有满足条件的了
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return res