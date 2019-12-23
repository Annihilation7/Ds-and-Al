# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 11:41am


'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        归并排序的思想，很简单
        '''
        dummy_head = ListNode(-1)
        l1_cur = l1
        l2_cur = l2
        pre_node = dummy_head

        while l1_cur is not None or l2_cur is not None:
            if l1_cur is None:
                pre_node.next = l2_cur
                return dummy_head.next
            if l2_cur is None:
                pre_node.next = l1_cur
                return dummy_head.next

            if l1_cur.val <= l2_cur.val:
                pre_node.next = l1_cur
                l1_cur = l1_cur.next
            else:
                pre_node.next = l2_cur
                l2_cur = l2_cur.next
            pre_node = pre_node.next

        return dummy_head.next