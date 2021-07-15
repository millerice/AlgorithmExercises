# -*- coding: utf-8 -*-
# @Time : 7/15/21 8:41 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_547_number_of_provinces.py
# @Software: PyCharm

"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，
那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 方法一
class Solution_1(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # 并查集问题
        uf = UnionFind()
        # 依次遍历元素，判断其是否为1，将为1的集合合并起来
        for i in range(len(isConnected)):
            # 添加集合
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
        # 返回省份数量
        return uf.num_of_sets


# 并查集模型
class UnionFind:
    def __init__(self):
        # 所有节点的父节点
        self.father = {}
        # 记录集合的数量
        self.num_of_sets = 0

    # 查找父节点并实现路径压缩
    def find(self, x):
        root = x
        # 查找当前节点父节点
        while self.father[root] != None:
            root = self.father[root]
        # 路径压缩
        while x != root:
            x, self.father[x] = self.father[x], root
        # 返回当前节点的父节点
        return root

    # 合并两个集合
    def merge(self, x, y):
        # 分别找到x、y的父节点
        root_x, root_y = self.find(x), self.find(y)
        # 判断x、y的父亲节点是不是同一个，不是的话则将x集合合并到y集合上
        if root_x != root_y:
            self.father[root_x] = root_y
        # 集合的数量减一
        self.num_of_sets -= 1

    # 添加新集合
    def add(self, x):
        # 判断节点是否已存在
        if x not in self.father:
            # 让新节点的父节点等于None
            self.father[x] = None
            # 集合数量加一
            self.num_of_sets += 1


# 方法二
class Solution_2:
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # 并查集问题
        # 查找父节点
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # 合并两个集合
        def union(x, y):
            parent[find(x)] = find(y)

        provinces = len(isConnected)
        parent = list(range(provinces))

        # 依次遍历元素，判断其是否为1，将为1的集合合并起来
        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)
        # 返回结果
        res = sum(parent[i] == i for i in range(provinces))
        return res




