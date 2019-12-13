# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-14 01:00am


'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？ 能呀
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        ofset指针方法
        删除节点一定要拿到待删除节点的前一个节点哦
        '''
        dummyhead = ListNode(-1)
        dummyhead.next = head

        offset_node = dummyhead
        while n > 0:
            offset_node = offset_node.next
            n -= 1
        cur_node = dummyhead
        while offset_node.next is not None:
            offset_node = offset_node.next
            cur_node = cur_node.next

        del_node = cur_node.next
        cur_node.next = del_node.next
        del_node.next = None

        return dummyhead.next
