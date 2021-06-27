# -*- coding: utf-8 -*-
# @Time : 6/27/21 11:55 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_142_linked_list_cycle_ii.py
# @Software: PyCharm

"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，
则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 定义快慢两个指针
        fast, slow = head, head
        # 循环遍历
        while True:
            # 判断fast是否已经走到头了
            if not (fast and fast.next):
                return
            # 快指针每次两步，慢指针每次一步
            fast, slow = fast.next.next, slow.next
            # 判断快慢指针是否相遇
            if fast == slow:
                break
        # 让fast等于head，快指针从头走到环的入口处，刚好会与环内的慢指针相遇
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


