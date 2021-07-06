# -*- coding: utf-8 -*-
# @Time : 7/6/21 9:50 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_122_best_time_to_buy_and_sell_stock_ii.py
# @Software: PyCharm

"""
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心算法求解，只要当天的股价收益大于0，就买入
        # 定义天数
        dates = len(prices)
        # 天数少与两天则直接返回
        if dates < 2:
            return 0
        # 将初始收益定为0
        res = 0
        # 循环遍历每天的股价
        for i in range(1, dates):
            profit = prices[i] - prices[i - 1]
            # 如果当天的股价收益大于0，则买入
            if profit > 0:
                res += profit
        return res
