# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 08:24:50 2019

@author: DELL

4_4_26_复杂链表的复制

题目：复杂链表的复制

题：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

没理解

"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        
        
class Solution:
    
    ###### 方案1
    # 返回 RandomListNode
    def Clone_1(self, pHead):
        # write code here
        import copy
        return copy.deepcopy(pHead)
    
    
    
    ###### 方案2
    def Clone_2(self, pHead):
        # write code here
        if  pHead==None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)
    
    def CloneNodes(self,pHead):
        '''
        复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
        '''
        pNode=pHead
        while pNode:
            pCloned=RandomListNode(0)
            pCloned.label=pNode.label
            pCloned.next=pNode.next

            pNode.next=pCloned
            pNode=pCloned.next
    
    def ConnectRandomNodes(self,pHead):
        '''
        将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针的后一个结点
        '''
        pNode=pHead
        while pNode:
            pCloned=pNode.next
            if pNode.random!=None:
                pCloned.random=pNode.random.next
            pNode=pCloned.next

    def ReconnectNodes(self,pHead):
        '''
        拆分链表：将原始链表的结点组成新的链表, 复制结点组成复制后的链表
        '''
        pNode=pHead
        pClonedHead=pClonedNode=pNode.next
        pNode.next = pClonedNode.next
        pNode=pNode.next
        while pNode:
            pClonedNode.next=pNode.next
            pClonedNode=pClonedNode.next
            pNode.next=pClonedNode.next
            pNode=pNode.next
        return pClonedHead
    
    
    
    ######## 方案3
    def Clone_3(self, pHead):
        # write code here
        if  pHead==None:
            return None
        newNode=RandomListNode(pHead.label)
        newNode.random=pHead.random
        newNode.next=self.Clone_3(pHead.next)
        return newNode
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    