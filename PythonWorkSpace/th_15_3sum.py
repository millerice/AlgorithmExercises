# -*- coding: utf-8 -*-
# @Time : 7/3/21 9:08 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_15_3sum.py
# @Software: PyCharm

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 如果长度不够3，则直接退出
        if len(nums) < 3:
            return []
        # 对数组进行排序
        nums.sort()
        # 定义一个set集合（集合中元素不能重复）
        res = set()
        # 使用枚举遍历数组
        for i, v in enumerate(nums[:-2]):
            # 如果当前元素和上一个元素重复，则继续判断下一个元素
            if i >= 1 and v == nums[i-1]:
                continue
            # 定义一个空字典
            d = {}
            # 遍历数组中的元素（从第二个元素开始）
            for x in nums[i+1:]:
                # 判断x元素是否已存在字典中
                if x not in d:
                    # 不存在则将-v-x加入到字典中
                    d[-v-x] = 1
                else:
                    # 将结果加入到res集合中
                    res.add((v, -v-x, x))
            print(d)
        # 返回最终结果
        return map(list, res)


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print([res for res in solution.threeSum(nums)])


