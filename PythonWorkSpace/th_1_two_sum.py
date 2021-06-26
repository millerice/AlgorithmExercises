# -*- coding: utf-8 -*-
# @Time : 6/26/21 10:55 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_1_two_sum.py
# @Software: PyCharm

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = nums[i]
            y = target - nums[i]
            nums[i] = "*"
            if y in nums:
                return [i, nums.index(y)]
            nums[i] = temp
        return [0, 0]
