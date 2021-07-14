# -*- coding: utf-8 -*-
# @Time : 7/14/21 9:05 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_200_number_of_islands.py
# @Software: PyCharm

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 并查集问题，找带头大哥
        if not grid or not grid[0]:
            return 0
        # 初始化网格
        uf = UnionFind(grid)
        # 定义上下左右四个坐标参数
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        # 遍历每一个格子中的数
        for i in range(m):
            for j in range(n):
                # 如果等于0则跳过
                if grid[i][j] == '0':
                    continue
                # 如果等于1，则遍历其上下左右四个方向的格子，如果格子中的数据也等于1，则合并在一起
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == '1':
                        uf.union(i * n + j, nr * n + nc)
        # 返回连通分量的数目
        return uf.count


# 定义一个并查集的类
class UnionFind:
    # 初始化函数
    def __init__(self, grid):
        # 获取表格的长宽
        m, n = len(grid), len(grid[0])
        # 定义count 记录连通总数
        self.count = 0
        # 定义一个存储岛屿的列表，初始值为-1，长度为m*n
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        # 遍历每一行
        for i in range(m):
            # 遍历每一列
            for j in range(n):
                # 判断当前格子的元素是否等于1
                if grid[i][j] == '1':
                    # 让当前格子的老大，等于它自己
                    self.parent[i*n + j] = i * n + j
                    # count 数量加1
                    self.count += 1

    # 查找（找老大）
    def find(self, i):
        # 判断第i个格子是否指向自己
        if self.parent[i] != i:
            # 继续查找
            self.parent[i] = self.find(self.parent[i])
        # 返回根
        return self.parent[i]

    # 合并
    def union(self, x, y):
        # x的根节点
        rootx = self.find(x)
        # y的根节点
        rooty = self.find(y)
        # 如果x、y不是同一个老大，则进行合并
        if rootx != rooty:
            # 路径压缩，将路径短的合并到路径长的上面去
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            if self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            # 连通分量的数量减1
            self.count -= 1
