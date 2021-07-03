# -*- coding: utf-8 -*-
# @Time : 7/3/21 4:22 PM
# @Author : icebear
# @Email : millerkai@163.com
# @File : th_20_valid_parentheses.py
# @Software: PyCharm

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 如果s的长度是个奇数，则直接返回
        if len(s) & 1 == 1:
            return False
        # 利用栈进行实现
        stack = list()
        # 定义一个括号的字典
        pare_dict = {")": "(", "}": "{", "]": "["}
        # 左右括号的个数为 len(s)/2
        left_len = len(s)/2
        # 遍历输入的字符串s
        for pare in s:
            # 判断括号是否为右括号，且左右括号是否匹配
            if pare in pare_dict:
                if not stack or stack[-1] != pare_dict[pare]:
                    return False
                stack.pop()
            # 将左括号压入栈中，并将左括号可用数量减一
            else:
                # 判断是否还有可用的左括号
                if left_len:
                    stack.append(pare)
                    left_len -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "()[{]{{}"
    print(solution.isValid(s))

