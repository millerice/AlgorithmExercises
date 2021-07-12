# -*- coding: utf-8 -*-
# @Time : 7/12/21 8:34 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_191_number_of_1_bits.py
# @Software: PyCharm

"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 位运算问题
        res = 0
        while n:
            # 每次消去最末尾的1
            n &= (n-1)
            res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(3))
