# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-16 11:46pm


'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        维基百科的答案。。。照着流程做的，但是不是很明白到底是什么意思
        """
        max_j = -1
        for j in range(len(nums) - 1, 0, -1):
            if nums[j] > nums[j - 1]:
                max_j = j - 1
                break
        if max_j == -1:
            self.reverse(nums, 0, len(nums) - 1)
            return
        k = -1
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > nums[max_j]:
                k = j
                break
        nums[k], nums[max_j] = nums[max_j], nums[k]
        self.reverse(nums, max_j + 1, len(nums) - 1)

    def reverse(self, alist, left, right):
        while left < right:
            alist[left], alist[right] = alist[right], alist[left]
            left += 1
            right -= 1

