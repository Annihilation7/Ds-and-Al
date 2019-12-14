# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 12:29pm


'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        两个指针顺序往下撸应该就可以了
        '''
        dummyhead = ListNode(-1)
        dummyhead.next = head

        pre_node = dummyhead
        cur_node = pre_node.next

        while cur_node and cur_node.next:
            next_node = cur_node.next.next
            pre_node.next = cur_node.next
            cur_node.next.next = cur_node
            cur_node.next = next_node

            pre_node = cur_node
            cur_node = next_node

        return dummyhead.next