# -*- coding: utf-8 -*-
# @Time : 7/13/21 8:48 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_120_triangle.py
# @Software: PyCharm

"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标
相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 动态规划问题
        # 状态定义：dp[i][j]  dp[i+1][j] dp[i+1][j+1]
        # 状态方程：min_sum += min(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]
        if not triangle:
            return 0
        # 定义一个结果列表，默认为triangle最后一层
        res = triangle[-1]
        n = len(triangle)
        # 从倒数第二层开始向上遍历
        for i in range(n - 2, -1, -1):
            # 遍历第i行的每一列
            for j in range(len(triangle[i])):
                # 取每一层中最小的值，与上一层相邻的值相加
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


if __name__ == '__main__':
    solution = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(solution.minimumTotal(triangle))
