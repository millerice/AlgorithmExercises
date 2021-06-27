# -*- coding: utf-8 -*-
# @Time : 6/27/21 2:18 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_25_reverse_nodes_in_k_group.py
# @Software: PyCharm

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 创建一个空节点,leetcode中执行时，注释掉下面一行
        ListNode = "empty node"
        pre_temp = ListNode(0)
        pre_temp.next = head
        pre = pre_temp

        # 链表反转
        while head:
            tail = pre
            # 判断剩余链表长度是否大于k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return pre_temp.next
            # 设置一个临时变量，记录第n个k长度链表的尾部元素
            temp = tail.next
            # 链表反转
            head, tail = self.reverse(head, tail)
            # 把反转后的子链表，接入原链表中
            pre.next, tail.next, pre = head, temp, tail
            head = tail.next
        return pre_temp.next

    def reverse(self, head, tail):
        cur, prev = head, tail.next
        while prev != tail:
            cur.next, prev, cur = prev, cur, cur.next
        return tail, head




