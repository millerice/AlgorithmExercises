# -*- coding: utf-8 -*-
# @Time : 6/27/21 9:30 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_232_implement_queue_using_stacks.py
# @Software: PyCharm

"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 定义两个栈
        self.a = []
        self.b = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # 压栈前先将b栈清空
        while self.b:
            self.a.append(self.b.pop())
        self.a.append(x)
        # 再将a栈中的元素弹出，放入b栈中。目的是将所有元素都先放入b栈中，让a栈为空，
        # 方便下面的push操作，避免元素顺序混乱
        while self.a:
            self.b.append(self.a.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # 从b栈栈顶弹出元素
        return self.b.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # 查看b栈中最后一个压入的元素
        return self.b[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # 判断b栈的长度是否为0
        return len(self.b) == 0
