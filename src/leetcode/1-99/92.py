# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-23 10:43pm


'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyhead = ListNode(-1)
        dummyhead.next = head

        pre_node = dummyhead
        cur_node = dummyhead.next

        for i in range(m - 1):
            pre_node = pre_node.next
            cur_node = cur_node.next

        rev_cur_node = cur_node
        rev_new_head = None
        for i in range(n - m + 1):
            next_node = rev_cur_node.next
            rev_cur_node.next = rev_new_head
            rev_new_head = rev_cur_node
            rev_cur_node = next_node

        pre_node.next = rev_new_head
        cur_node.next = rev_cur_node

        return dummyhead.next