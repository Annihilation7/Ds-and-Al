# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 12:35am


'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        与3sum大同小异，区别就是现在固定两个数了，原先是固定一个数
        边界条件有一点点变化，稍微有点绕哦
        '''
        res = []

        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1
                while left < right:
                    tmp_res = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp_res == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp_res > target:
                        right -= 1
                    else:
                        left += 1

        return res


if __name__ == '__main__':
    test = Solution()
    test_case = [1, -2, -5, -4, -3, 3, 3, 5]
    print(test.fourSum(test_case, -11))


