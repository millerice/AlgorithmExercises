# -*- coding: utf-8 -*-
# @Time : 7/11/21 3:21 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_212_word_search_ii.py
# @Software: PyCharm

"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
"""


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 前缀树回溯的解法
        # 定义前缀树
        tree = dict()
        # 将每个字母都放入前缀树中
        for word in words:
            t = tree
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['word'] = word

        # 定义一个结果列表
        res = []
        # 利用广度优先遍历查找目标单词是否在前缀树中
        def bfs(i, j):
            # 获取每个字母
            ch = board[i][j]
            # 定义一个队列（坐标，单词）
            queue = [([(i, j)], tree[ch])]
            # 遍历队列
            while queue:
                # 定义一个临时列表
                tmp = []
                # 分别从队列中取出坐标列表和单词列表
                for coor, t in queue:
                    # 判断单词是否等于结束标识
                    if 'word' in t:
                        res.append(t['word'])
                    # 取出x,y的坐标
                    xi, yi = coor[-1]
                    # 遍历该坐标的周边点，如果合法则加入到临时列表中
                    for x, y in [(xi + 1, yi), (xi - 1, yi), (xi, yi + 1), (xi, yi - 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) not in coor and board[x][y] in t:
                            tmp += [(coor + [(x, y)], t[board[x][y]])]
                # 将临时列表赋值给队列
                queue = tmp
        # 确定二维字符网格的边界
        m, n = len(board), len(board[0])
        # 循环遍历二维字符网格的每一个单词，并判断其是否存在于前缀树中，是，调用bfs
        for i in range(m):
            for j in range(n):
                if board[i][j] in tree:
                    bfs(i, j)
        # 返回去重的结果列表
        return list(set(res))


if __name__ == '__main__':
    solution = Solution()
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(solution.findWords(board, words))
