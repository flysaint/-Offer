# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:18:07 2019

@author: DELL

题目：反转链表

题：输入一个链表，反转链表并输出反转后链表的头节点。

解题思路：注意反转时出现断裂现象，定义3个指针，
分别指向当前遍历到的节点pNode、
它的前一个节点pPrev及后一个节点pNext。

我的问题
1. 怎么通过一个Node，让链表不断的情况下， 使得前一个关联后一个。
2. 怎么用同样长度的Link将原来的装进去。

思路和理解
将 pPrev,pNode,pNext
1. 箱子的组成。对象地址，下一个对象的地址。
2. 对箱子赋值。就是把另外一个箱子里的东西，复制一套，覆盖掉这个箱子里的所有东西。
3. 

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
          
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):         
        pNode = pHead
        pPrev = None
        pReverseHead = None
        
        while(pNode):
            pNext = pNode.next
            if(not pNext):
                pReverseHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        
        return pReverseHead
        
            
            














'''
         
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReversedHead=None
        pNode=pHead
        pPrev=None
        
        while pNode:
            pNext=pNode.next
            if not pNext:
                pReversedHead=pNode
            pNode.next=pPrev
            pPrev=pNode
            pNode=pNext
        return pReversedHead        
    
'''  
               


if __name__ == "__main__":
    
    values = [1,2,3,4,5]
    
    link1 = LinkList()
    link1.initLinkList(values)
    '''
    pHead = link1.head
    pNode = pHead
    pPrev = None
    pNext = pNode.next
    
    print("pPrev = {}".format(pPrev))
    print("pNode = {}".format(pNode))
    print("pNext = {}".format(pNext))
    
    pNode.next=pPrev
    pPrev=pNode
    pNode=pNext
    
    print("pPrev = {}".format(pPrev))
    print("pNode = {}".format(pNode))
    print("pNext = {}".format(pNext))
    
    print("pPrev.next = {}".format(pPrev.next))
    print("pNode.next = {}".format(pNode.next))
    print("pNext.next = {}".format(pNext.next))
    
    '''
    
    link2 = LinkList()
    link2.initLinkList(values)
    print("we are process link1 :")
    while(link1.head):
        #print(link1.head)
        
        print(link1.head.val)
        link1.head = link1.head.next
        
    s = Solution()

    link2.head = s.ReverseList(link2.head)    
    print("we are process link2 :")   
    while(link2.head):
        
        print(link2.head.val)
        link2.head = link2.head.next
        
    
    
        
        

    
    
    
    
    
    
    
    
    
    
    


