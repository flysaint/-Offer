# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:12:45 2019

@author: DELL

4_3_24_二叉搜索树的后序遍历

题：二叉搜索树的后序遍历序列

题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:03:39 2019

@author: DELL

4_3_23_从上往下打印二叉树

肯定是递归或者循环


怎么初始化二叉树

定义后手动进行关联，或者先生成节点

"""

        
'''
怎么实现递归
肯定是递归
只要还有左孩子，就不停的遍历。
在同一层中，

问题是什么？

1. 区分大小。
2. 保持连续。怎么保持连续？非连续直接返回错误？怎么判断是否非连续？

和连续性没关系，关键在找分割节点

'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST_1(self, sequence):
        # write code here
        if not sequence or len(sequence)<=0:
            return False
        if len(sequence) == 1:
            return True
        
        root=sequence[-1]
        # 找出分割节点
        seq_index = -1
        for i in range(1,len(sequence)):
            if sequence[i-1] < root and sequence[i] > root:
                seq_index = i
                break
        
        # 考虑一边，全部大，全部小的问题
        left_flag = True
        if i >0:
            left_flag = self.VerifySquenceOfBST_1(sequence[:seq_index])    
        right_flag = True
        if i < len(sequence) -1:
            right_flag = self.VerifySquenceOfBST_1(sequence[seq_index:len(sequence)-1])
        
        return left_flag and right_flag
        

    def VerifySquenceOfBST_2(self, sequence):
        # write code here
        if not sequence or len(sequence)<=0:
            return False
        root=sequence[-1]
        i=0
        
        #找出左小右大的分界点i,此时i属于右子树
        for node in sequence[:-1]:
            if node > root:
                break
            i+=1
        
        #如果在右子树中有比根节点小的值，直接返回False
        for node in sequence[i:-1]:
            if node < root:
                return False
        #判断左子树是否为二叉搜索树
        left=True
        if i>0:
            left=self.VerifySquenceOfBST_2(sequence[:i])
        #判断右子树是否为二叉搜索树
        right=True
        if i<len(sequence)-1:
            right=self.VerifySquenceOfBST_2(sequence[i:-1])

        return left and right



if __name__ == "__main__":
    
    nodes = [5,7,6,8,9,11,10]
    s = Solution()
    print(s.VerifySquenceOfBST_1(nodes))
    print(s.VerifySquenceOfBST_2(nodes))
    #pretty_print(node1)
  
    
    
    
    
    
