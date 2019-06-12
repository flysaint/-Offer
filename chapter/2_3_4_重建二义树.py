# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:20:00 2019

@author: DELL

要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值

思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，
00右边是右子树，然后递归的处理左边和右边

提示：二叉树结点，以及对二叉树的各种操作，测试代码见six.py
案例：输入先序遍历 {1,2,4,7,3,5,6,8}中序遍历 {4,7,2,1,5,3,8,6}

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root=TreeNode(pre[0])
        val=tin.index(pre[0])
        
        root.left=self.reConstructBinaryTree(pre[1:val+1],tin[:val])
        root.right=self.reConstructBinaryTree(pre[val+1:],tin[val+1:])
        return root
    
    
    
if __name__ == '__main__':
    
    reConstructBinaryTree()
    
    
    
    