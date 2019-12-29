# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-23 10:38pm


'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        cur_node = head

        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = new_head
            new_head = cur_node
            cur_node = next_node

        return new_head