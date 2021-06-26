# -*- coding: utf-8 -*-
# @Time : 6/26/21 10:02 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : single_linked_list.py
# @Software: PyCharm
from linked_list import Node


class SingleLinkedList(object):
    def __init__(self):
        self._head = None    # 初始化链表为空表
        self._size = 0

    def is_empty(self):
        return self._head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            self._head = temp   # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.get_next() != None:
                current = current.get_next()   # 遍历链表
            current.set_next(temp)   # 此时current为链表最后的元素
        return temp

    def search(self, item):
        current = self._head
        founditem = False
        while current != None and not founditem:
            if current.get_item() == item:
                founditem = True
            else:
                current = current.get_next()
        return founditem

    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.get_item() == item:
                found = True
            else:
                current = current.get_next()
        if found:
            return count
        else:
           print('%s is not in linkedlist') % item

    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.get_item() == item:
                if not pre:
                    self._head = current.get_next()
                else:
                    pre.set_next(current.get_next())
                break
            else:
                pre = current
                current = current.get_next()

    def insert(self, pos, item):
       if pos <= 1:
           self.add(item)
       elif pos > self.size():
           self.append(item)
       else:
           temp = Node(item)
           count = 1
           pre = None
           current = self._head
           while count < pos:
               count += 1
               pre = current
               current = current.get_next()
           pre.set_next(temp)
           temp.set_next(current)
