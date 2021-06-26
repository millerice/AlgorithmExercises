# -*- coding: utf-8 -*-
# @Time : 6/26/21 10:26 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_141_linked_list_cycle.py
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 给定一个链表，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 定义两个指针，慢指针一次走一步，快指针一次走两步
        fast = slow = head
        # 循环遍历（slow、fast、fast.next不等于None）
        while slow and fast and fast.next:
            # 慢指针
            slow = self.next
            # 快指针
            fast = self.next.next
            # 判断两个指针是否指向同一个地址（相同，说明快指针又走回来了，存在环）
            if slow is fast:
                return True
        return False

