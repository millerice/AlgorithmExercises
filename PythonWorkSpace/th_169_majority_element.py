# -*- coding: utf-8 -*-
# @Time : 7/5/21 11:11 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_169_majority_element.py
# @Software: PyCharm

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义两个变量
        count, res = 0, None
        # 遍历nums
        for num in nums:
            # 如果count=0，则将res重新赋值
            if count == 0:
                res = num
            # 判断res是否等于num，是则加1，不是则减1
            count += (1 if res == num else -1)
        return res


