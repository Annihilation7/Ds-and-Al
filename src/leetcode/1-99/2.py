'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        一起从头遍历两个链表，带着进位加就完事了。
        注意1：两个链表的长度可能不一样，多余的部分长度小的节点值设成0即可。
        注意2：别忘了最后的进位。
        '''
        cur1 = l1
        cur2 = l2
        c = 0
        dummyhead = ListNode(-1)  # dummyhead
        res_node = dummyhead

        while cur1 is not None or cur2 is not None:
            num1 = 0 if cur1 is None else cur1.val
            num2 = 0 if cur2 is None else cur2.val
            _sum = num1 + num2 + c
            true_sum = _sum % 10
            c = _sum // 10
            res_node.next = ListNode(true_sum)
            if cur1 is not None:
                cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next
            res_node = res_node.next

        if c == 1:  # 最后有可能会有1个进位
            res_node.next = ListNode(1)

        return dummyhead.next