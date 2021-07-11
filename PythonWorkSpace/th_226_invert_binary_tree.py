# -*- coding: utf-8 -*-
# @Time : 7/8/21 8:07 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_226_invert_binary_tree.py
# @Software: PyCharm


class BinaryTree(object):
    # 二叉树
    def __init__(self, item=None, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right


class TreeReverse(object):
    # 二叉树反转，采用递归的方式解决
    def binary_tree_reverse(self, root):
        # 判断二叉树是否为空
        if root is None:
            return
        # 获取左节点
        left = self.binary_tree_reverse(root.left)
        # 获取右节点
        right = self.binary_tree_reverse(root.right)
        # 左右节点互换
        root.left, root.right = right, left
        # 返回反转后的二叉树
        return root


if __name__ == '__main__':
    root = BinaryTree(3, BinaryTree(5, BinaryTree(8, BinaryTree(1), BinaryTree(4)), BinaryTree(2)))
    tree_reverse = TreeReverse()
    print(tree_reverse.binary_tree_reverse(root))











