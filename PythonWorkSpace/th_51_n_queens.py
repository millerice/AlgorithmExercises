# -*- coding: utf-8 -*-
# @Time : 7/7/21 10:46 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_51_n_queens.py
# @Software: PyCharm

"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 判断n的数量
        if n < 1:
            return []
        # 定义一个结果列表
        self.result = []
        # 定义三个集合，用来存储皇后的位置
        self.cols = set()
        self.pie = set()
        self.na = set()
        # 采用深度优先遍历的从第一行开始遍历
        self.DFS(n, 0, [])
        # 返回棋盘形状
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # 如果行数大于n，说明行数已经遍历完了，可以返回结果了
        if row >= n:
            self.result.append(cur_state)
            return
        # 遍历n列，让皇后在每一列都待一遍
        for col in range(n):
            # 如果皇后在 横、撇、捺 的位置上已经存在另一个皇后了，那么直接进行下一个位置的尝试
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            # 将当前行的位置，添加到行集合中
            self.cols.add(col)
            # 将当前撇的位置，添加到撇集合中
            self.pie.add(row + col)
            # 将当前捺的位置，添加到捺集合中
            self.na.add(row - col)
            # 调用DFS进行下一行的遍历
            self.DFS(n, row + 1, cur_state + [col])
            # 将横、撇、捺集合中的位置清楚掉
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        # 定义一个列表
        board = []
        # 遍历结果列表
        for res in self.result:
            # 构造棋盘
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        # 将结果返回
        return [board[i: i + n] for i in range(0, len(board), n)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))

