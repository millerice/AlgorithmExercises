# -*- coding: utf-8 -*-
# @Time : 7/5/21 8:16 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_50_powx_n.py
# @Software: PyCharm

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # x等于0，直接返回0
        if x == 0:
            return 0
        # n为负值，x转为其倒数
        if n < 0:
            x, n = 1/x, -n
        res = 1
        # 循环n，判断n是否为奇数，奇数时乘一个x，每次向右移动1位
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2, 5))


