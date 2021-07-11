# -*- coding: utf-8 -*-
# @Time : 7/11/21 9:19 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_52_n_queens_ii.py
# @Software: PyCharm

"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 剪枝问题
        # 定义列、撇、捺三个方向集合
        lie, pie, na = set(), set(), set()
        # 让皇后分别处于棋盘上每一行、每一列，判断其是否合法
        # 合法：皇后的横、竖、撇、捺上只能存在一个皇后
        # 定义一个结果集
        res = [0]
        def back_track(n_row):
            # 回溯到最后一行则退出
            if n_row == n:
                res[0] += 1
                return
            # 判断每一行、每一列元素
            for col in range(n):
                if (col not in lie) and (col + n_row not in pie) and (col - n_row not in na):
                    # 将其他皇后不能存在的位置添加到对应的集合中
                    lie.add(col)
                    pie.add(col + n_row)
                    na.add(col - n_row)
                    # 判断下一行皇后的位置
                    back_track(n_row + 1)
                    # 将集合中皇后位置清空
                    lie.remove(col)
                    pie.remove(col + n_row)
                    na.remove(col - n_row)
        # 从第一行开始执行
        back_track(0)
        return res[0]
