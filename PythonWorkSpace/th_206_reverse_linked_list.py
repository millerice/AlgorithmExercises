# -*- coding: utf-8 -*-
# @Time : 6/26/21 8:56 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_206_reverse_linked_list.py
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# 来源：力扣（LeetCode）
# 链接：https://leetcode.com/problems/reverse-linked-list/


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


