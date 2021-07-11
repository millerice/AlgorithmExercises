# -*- coding: utf-8 -*-
# @Time : 7/11/21 8:57 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_104_maximum_depth_of_binary_tree.py
# @Software: PyCharm

"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 深度优先遍历解决
        # 递归结束条件，root是否为None
        if root is None:
            return 0
        else:
            # 递归遍历root左右节点
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            # 返回最大深度
            return max(left, right) + 1


