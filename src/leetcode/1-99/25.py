# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-15 07:19pm


'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
        不多说了，这个代码要及时复习，写了挺长时间的- -
        这是我过的第一道苦难题目，哈哈，再接再厉！
        '''
        dummy_head = ListNode(-1)
        dummy_head.next = head

        pre = dummy_head
        end = dummy_head
        while end is not None:
            k_copy = k
            while k_copy > 0 and end.next is not None:
                end = end.next
                k_copy -= 1
            if k_copy != 0:
                break
            start = pre.next
            next_node = end.next
            end.next = None
            pre.next = self._reverse(start)
            start.next = next_node
            pre = start
            end = start
        return dummy_head.next

    def _reverse(self, head):
        pre = head
        cur = head.next
        while cur is not None:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre