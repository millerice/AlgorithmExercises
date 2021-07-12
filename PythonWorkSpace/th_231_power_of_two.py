# -*- coding: utf-8 -*-
# @Time : 7/12/21 8:44 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_231_power_of_two.py
# @Software: PyCharm

"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 位运算问题
        # 如果 n = 2x次幂，那么满足 n的最高位为1，其余都为0。n-1的最高位为0，其余都为1。
        # 所以 n & n - 1 为0
        # 判断n是否小于等于1
        if n <= 1:
            return True
        return n & (n - 1) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(3))

