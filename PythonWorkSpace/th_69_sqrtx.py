# -*- coding: utf-8 -*-
# @Time : 7/11/21 10:31 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_69_sqrtx.py
# @Software: PyCharm

"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 利用二分查找解决
        # 判断x是否为0
        if x == 0:
            return 0
        left, right, res = 0, x, -1
        while left <= right:
            # 取中间值
            mid = (left + right) // 2
            # 判断中间值的平方与x的大小
            if mid*mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(8))

