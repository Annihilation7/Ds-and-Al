# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-24 08:47pm


'''
编写一个程序，找到两个单链表相交的起始节点。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_a = self._get_length(headA)
        length_b = self._get_length(headB)
        offset = abs(length_b - length_a)

        # 始终让A保证是长度较小的链表
        if length_a > length_b:
            headA, headB = headB, headA

        cur_a = headA
        cur_b = headB
        while offset:
            cur_b = cur_b.next
            offset -= 1

        while id(cur_a) != id(cur_b):
            cur_a = cur_a.next
            cur_b = cur_b.next

        return cur_a

    def _get_length(self, head):
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1
        return length