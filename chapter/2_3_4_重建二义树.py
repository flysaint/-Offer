# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:20:00 2019

@author: DELL

要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值

思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，
00右边是右子树，然后递归的处理左边和右边

提示：二叉树结点，以及对二叉树的各种操作，测试代码见six.py
案例：输入先序遍历 {1,2,4,7,3,5,6,8}中序遍历 {4,7,2,1,5,3,8,6}

重新用树将节点组合起来，返回根节点
"""

class Node:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
        

class Solution:
    def construct_tree(preorder=None, inorder=None):
        root = Node(preorder[0])
        
        root_index = inorder.index(root.val)
        
        root.left = construct_tree(preorder[1:root_index+1],inorder[0:root_index])
        root.right = construct_tree(preorder[root_index+1:],inorder[root_index+1:])
        
        return root


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def construct_tree(preorder=None, inorder=None):
    """
    构建二叉树
    步骤。
    1. 子树是否到头。确保先序遍历的子树和中序遍历的子树都还有孩子。否则返回None
    2. 获取根节点在中序遍历的序号。
    3. 获取左右子树。
    4. 使用当前先序遍历的节点作为新的根节点。
    5. 递归衍生左子树。递归衍生右子树。
    
    不断创建节点，让节点相连，并返回根节点的过程
    
    """
        if not preorder or not inorder:
            return None
        index = inorder.index(preorder[0])
        left = inorder[0:index]
        right = inorder[index+1:]
        root = TreeNode(preorder[0])
        root.left = construct_tree(preorder[1:1+len(left)], left)
        root.right = construct_tree(preorder[-len(right):], right)
        return root
    
    
    
if __name__ == '__main__':
    
    reConstructBinaryTree()
    list_a = [1,2,3,4,5,6,8]

    list_a.index(8)
    
    
    