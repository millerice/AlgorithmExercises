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
    # Method one
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = nums[i]
            y = target - nums[i]
            nums[i] = ""
            if y in nums:
                return [i, nums.index(y)]
            nums[i] = temp
        return [0, 0]

    # Method two
    def twoSum_2(self, nums, target):
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target-num], i]
            hash_table[nums[i]] = i
        return [0, 0]


if __name__ == '__main__':
    solu = Solution()
    # nums = [2, 7, 11, 34]
    nums = [0, 3, 3, 0]
    target = 6
    print(solu.twoSum_2(nums, target))
