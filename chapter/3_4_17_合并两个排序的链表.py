# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:49:24 2019

@author: DELL

3_4_17_合并两个排序链表

面试25题：
题目：合并两个排序的链表

题：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解题思路：递归，并需注意对空链表单独处理。

"""

class Node(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        

class LinkList(object):
    def __init__(self):
        self.head = None
        
    def initLinkList(self,values):
        self.head = Node(values[0])
        move = self.head
        
        for v in values[1:]:
            node = Node(v)
            move.next = node
            move = move.next



# 返回合并后列表
def MergeLink( pHead1, pHead2):
    # write code here
    if not pHead1:
        return pHead2
    elif not pHead2:
        return pHead1
    pMergedHead=None
    if (pHead1.val<pHead2.val):
        pMergedHead=pHead1
        pMergedHead.next=Merge(pHead1.next,pHead2)
    else:
        pMergedHead=pHead2
        pMergedHead.next=Merge(pHead1,pHead2.next)
        
    return pMergedHead

          
class Solution:
    # 返回合并后列表
    def MergeLink(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        pMergedHead=None
        if (pHead1.val<pHead2.val):
            pMergedHead=pHead1
            pMergedHead.next=self.Merge(pHead1.next,pHead2)
        else:
            pMergedHead=pHead2
            pMergedHead.next=self.Merge(pHead1,pHead2.next)
            
        return pMergedHead
            

    # 返回合并后列表'
    # 本次选择哪个节点。下次选择哪个节点
    def Merge(self, pHead1, pHead2):
        # write code here
        if not self.pHead1:
            return self.pHead2
        elif not self.pHead2:
            return self.pHead1
        pMergedHead=None
        if (self.pHead1.val< self.pHead2.val):
            pMergedHead=self.pHead1
            pMergedHead.next=self.Merge(pHead1.next,pHead2)
        else:
            pMergedHead=self.pHead2
            pMergedHead.next=self.Merge(pHead1,pHead2.next)
            
        return pMergedHead
    
            
if __name__ == "__main__":
    
    values = [1,2,3,4,5]
    
    link1 = LinkList()
    link1.initLinkList(values)
    
    
    values = [1,2,3,4,5]
    
    link2 = LinkList()
    link2.initLinkList(values)
    
    #s = Solution()
    #link = s.MergeLink(link1,link2)
    link = MergeLink(link1,link2)
    while(link):
        print(link.val)
        link = link.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    