# -*- coding: utf-8 -*-
# @Time : 7/15/21 9:47 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_146_lru_cache.py
# @Software: PyCharm

"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
    LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
    int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，
    则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，
    从而为新的数据值留出空间。

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class DLinkedNode:
    # 双向链表
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # 哈希表 + 双向链表 解决
        # 定义一个哈希表
        self.cache = dict()
        # 定义一个链表的伪头部和伪尾部
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        # 定义链表
        self.head.next = self.tail
        self.tail.prev = self.head
        # lurcache的总容量
        self.capacity = capacity
        # 定义lurcache已使用的容量
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 判断key是否在哈希表中存在
        if key not in self.cache:
            return -1
        # 如果存在，则先通过hash表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 判断key是否在hash表中存在
        if key not in self.cache:
            # 如果不存在，则创建一个新节点
            node = DLinkedNode(key, value)
            # 将新节点添加到hash表中
            self.cache[key] = node
            # 将新节点添加到双向链表的头部
            self.addToHead(node)
            # lrucache已用容量加1
            self.size += 1
            # 判断已用容量是否大于总容量
            if self.size > self.capacity:
                # 如果超出总容量，则删除双向链表尾部的节点
                removed = self.removeTail()
                # 删除hash表中对应的值
                self.cache.pop(removed.key)
                # 已用容量减一
                self.size -= 1
        else:
            # 如果key存在，则先通过hash表定位，再更新value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    # 在双向链表的头部添加一个节点
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除双向链表中的指定节点
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 将节点移动到双向链表的头部
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    # 删除双向链表的尾部节点
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
