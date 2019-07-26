# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:49:24 2019

@author: DELL


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
            
class Solution(object):
    
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
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
    
    
    def mergeLink(self,linkA,linkB):
        headA = linkA.head
        headB = linkB.head
        
        if headA.val > headB.val:
            node = Node(headB.val)
            headB = headB.next
        else:
            node = Node(headA.val)
            headA = headA.next
        
        head = node
            
        while(headA and headB):
            if headA.val > headB.val:
                node.next = Node(headB.val)
                headB = headB.next
                node  = node.next
            else:
                node.next = Node(headA.val)
                headA = headA.next
                node = node.next
                
        while(headA):
            node.next = Node(headA.val)
            headA = headA.next
            node = node.next
            
        while(headB):
            node.next = Node(headB.val)
            headB = headB.next
            node = node.next
            
        return head
            
            

if __name__ == "__main__":
    
    values = [1,2,3,4,5]
    
    link1 = LinkList()
    link1.initLinkList(values)
    
    
    values = [1,2,3,4,5]
    
    link2 = LinkList()
    link2.initLinkList(values)
    
    s = Solution()
    link = s.mergeLink(link1,link2)
    while(link):
        print(link.val)
        link = link.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    