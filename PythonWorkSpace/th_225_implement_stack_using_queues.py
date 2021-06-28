# -*- coding: utf-8 -*-
# @Time : 6/28/21 9:55 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_225_implement_stack_using_queues.py
# @Software: PyCharm

"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。
"""
from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 定义两个队列q1、q2
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # 将x元素添加到q1中
        self.q1.append(x)
        # 将q2中的元素也都添加到q1中
        while self.q2:
            self.q1.append(self.q2.popleft())
        # 将q1和q2进行互换
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # 从队列的左端弹出一个元素，模拟栈的头部弹出元素
        return self.q2.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # 返回q2下标为0的元素
        return self.q2[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        # 判断q2的长度
        return len(self.q2) == 0
