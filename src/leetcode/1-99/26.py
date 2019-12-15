# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-15 09:36pm


'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        因为数组是排好序的，所以单索引就可以啦，但是时间复杂度是O(N^2)的。。
        采用双指针方法，可以将时间复杂度降低到O(N)
        '''

        # 下面这个我写的是O(n^2)的。。不是很好
        # index = 0
        # while index < len(nums):
        #     while index + 1 < len(nums) and nums[index + 1] == nums[index]:
        #         nums.pop(index + 1)
        #     index += 1
        # return len(nums)


        '''
        双指针巧妙的赋值方法替代pop方法，真的非常优秀
        '''
        left = right = 0
        while right < len(nums):
            if nums[right] != nums[left]:
                if left + 1 < len(nums):
                    nums[left + 1] = nums[right]
                    left += 1
            right += 1
        return left + 1

