# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-08 01:18am


'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        利用哈希表存储每个元素的对于target的被减数以及索引，如果存在就表明符合相加为target
        的条件
        时间复杂度：O(n)
        '''
        record = {}

        for i in range(len(nums)):
            offset = target - nums[i]
            if nums[i] in record:
                return [record[nums[i]], i]
            else:
                record[offset] = i

        return []
