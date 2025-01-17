# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:31:31 2019

@author: DELL


3_4_18_树的子结构

题目：树的子结构

题：输入两棵二叉树A和B，判断B是不是A的子结构。

解题思路：递归，注意空指针的情况

输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构


分几种情况处理呢？

1. 如果到了当前节点上。当前节点相等，则继续判断左右孩子是否相等。

可以用递归实现。


寻找 第一课树上，有没有和第二树相等的部分


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if self.pRoot1 is None:
            return False
        
        if self.pRoot2 is None:
            return False
        
        if self.pRoot1.val == self.pRoot2.val:
            return self.DoesTree1haveTree2(self, pRoot1, pRoot2)
        else:
            return self.HasSubtree(self, pRoot1.left, pRoot2) or self.HasSubtree(self, pRoot1.right, pRoot2)
        
     
    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if self.pRoot1 is None:
            return False
        
        if self.pRoot2 is None:
            return True
        
        if self.pRoot1.val != self.pRoot2.val:
            return False
        
        if self.pRoot1.val == self.pRoot2.val:
            return self.DoesTree1haveTree2(self.pRoot1.left,self.pRoot2.left) and self.DoesTree1haveTree2(self.pRoot1.right,self.pRoot2.right)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    # 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    # 如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)

'''
pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))