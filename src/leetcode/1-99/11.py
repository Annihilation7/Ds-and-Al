# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-09 12:46am


'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。
在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        头尾双指针夹逼
        怎么边要看谁的下一条边比较长，因为往里缩的过程中，宽度是变小的，所以要用长度来弥补
        '''
        left_index = 0
        right_index = len(height) - 1
        max_area = -1

        while left_index < right_index:
            max_area = \
                max(max_area, self._cal_area(height, left_index, right_index))
            # 虽然宽度减小，但是尝试让较小的边的index移动，可能会获得更大的面积
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return max_area

    def _cal_area(self, height, left_index, right_index):
        '''
        左闭右闭区间
        '''
        return min(height[left_index], height[right_index]) * \
               (right_index - left_index)