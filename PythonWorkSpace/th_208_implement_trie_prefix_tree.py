# -*- coding: utf-8 -*-
# @Time : 7/11/21 2:41 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_208_implement_trie_prefix_tree.py
# @Software: PyCharm

"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
    Trie() 初始化前缀树对象。
    void insert(String word) 向前缀树中插入字符串 word 。
    boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
"""


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 定义一个包含26个空值的列表
        self.children = [None] * 26
        # 初始化终止条件
        self.isEnd = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self
        # 遍历word，取出每个单词的每个字母
        for ch in word:
            # 将每个字母转成数字，减a的意思是将asic码值的小写字母，都从0开始计数
            ch = ord(ch) - ord("a")
            # 判断该字母是否在当前层的列表中
            # 如果不在，则创建
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        # 最后一个节点的终止条件，设置为True
        node.isEnd = True

    def searchPrefix(self, prefix):
        # 查找前缀
        node = self
        # 遍历每个字母
        for ch in prefix:
            ch = ord(ch) - ord("a")
            # 不存在则返回None
            if not node.children[ch]:
                return None
            # 存在，将当前节点的单词赋给node，继续遍历下一个单词
            node = node.children[ch]
        # 将node返回
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # 遍历每个单词的每个字母
        # 如果遍历完成后，最后一个节点不为None而且isEnd为True，则返回True
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # 遍历前缀，如果前缀树中的字母都存在，则返回True
        return self.searchPrefix(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
