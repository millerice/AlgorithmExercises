# -*- coding: utf-8 -*-
# @Time : 7/6/21 10:07 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_860_lemonade_change.py
# @Software: PyCharm

"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，
也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lemonade-change
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 贪心算法
        # 定义两个变量，five ten 初始值为0
        five = ten = 0
        # 遍历 bills
        for bill in bills:
            # 判断bill是否为5，是的话5加1
            if bill == 5:
                five += 1
            # 判断bill是否为10，是的话，判断five是否为0
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            # 判断bill是否为20，是的话，判断five 和 ten 是否为0
            elif bill == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                # 判断five是否大于等于3
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
