# -*- coding: utf-8 -*-
# @Time : 7/12/21 9:05 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_338_counting_bits.py
# @Software: PyCharm

"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
"""


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 位运算
        # 奇数一定比前一个偶数多一个1
        # 偶数中1的个数和除以2之后的那个数一样多
        # 0 的二进制中 1 的个数为0
        # 定义一个结果列表, 初始值为0
        res = [0]
        # 遍历n
        for i in range(1, n + 1):
            # 奇数
            if i & 1 == 1:
                res.append(res[i - 1] + 1)
            # 偶数
            else:
                res.append(res[int(i/2)])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(12))









