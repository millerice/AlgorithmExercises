# -*- coding: utf-8 -*-
# @Time : 7/8/21 7:22 AM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_102_binary_tree_level_order_traversal.py
# @Software: PyCharm

"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 利用广度优先遍历的方法
        # 判断root是否为空
        if root is None:
            return []
        # 定义一个结果列表
        res = []
        # 定义一个队列，将root放入队列中
        queue = [root]
        # 遍历队列
        while queue:
            # 将队列当前层的元素取出，放入一个列表中
            curent_level_len = len(queue)
            curent_level_ele_list = []
            for i in range(curent_level_len):
                node = queue.pop(0)
                curent_level_ele_list.append(node.val)
                # 判断当前层元素是否有左右孩子，有的话将其重新放入队列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 将当前层元素放入结果列表中
            res.append(curent_level_ele_list)
        return res

