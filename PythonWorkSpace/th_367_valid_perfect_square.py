# -*- coding: utf-8 -*-
# @Time : 7/11/21 11:18 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_367_valid_perfect_square.py
# @Software: PyCharm

"""
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如  sqrt 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 判断num 是否小于2 (因为是正整数)
        if num < 2:
            return True
        # 利用二分查找解决
        # 定义left、right两个变量
        left, right = 2, num // 2
        # 判断left<=right
        while left <= right:
            # 定义一个中间变量
            mid = left + (right - left) // 2
            # 判断中间变量的平方与num的大小
            if mid*mid == num:
                return True
            elif mid*mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare(10))
