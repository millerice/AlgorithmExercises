# -*- coding: utf-8 -*-
# @Time : 7/12/21 9:40 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_70_climbing_stairs.py
# @Software: PyCharm

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划问题
        # 从结果往初始条件推
        # 状态定义：dp[n] dp[n-1] dp[n-2]
        # 第n阶台阶的结果等于 dp[n-1] + dp[n-2]
        # 状态方程：dp[n] = dp[n-1] + dp[n-2]
        # 第0和1阶台阶的走法都只有1种
        dp = [1, 1]
        # 统计走到n阶的走法（前闭后开，所以 n + 1）
        for i in range(2, n + 1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(3))


