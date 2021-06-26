# -*- coding: utf-8 -*-
# @Time : 6/26/21 9:52 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : linked_list.py
# @Software: PyCharm


class Node(object):
    __slots__ = ['_item', '_next']

    def __init__(self, item):
        self._item = item
        self._next = None

    def get_item(self):
        return self._item

    def get_next(self):
        return self._next

    def set_item(self, new_item):
        self._item = new_item

    def set_next(self, new_next):
        self._next = new_next

    def is_empty(self):
        return self._head == None


