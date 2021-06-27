# -*- coding: utf-8 -*-
# @Time : 6/27/21 10:11 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_24_swap_nodes_in_pairs.py
# @Software: PyCharm

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        reference: 超哥
        """
        # leetcode中执行，注释下面ListNode
        ListNode = '链表中 dummy node'
        result = ListNode(0)
        pre, pre.next = result, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return result.next
