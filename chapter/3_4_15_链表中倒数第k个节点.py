# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:29:33 2019

@author: DELL


面试22题：

题目：链表中倒数第k个节点

题：输入一个链表，输出该链表中倒数第k个结点。

解题思路：为了实现只遍历链表一次就能找到倒数第k个节点，我们可以定义两个指针。
让第一个指针先向前走k-1步，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。
由于两个指针的距离保持在k-1,当第一个指针到达链表的尾节点时，第二个指针刚好到达倒数第k个节点。

收获
定义

记住 
1. __init__ 主要是用来定义属性的。当然也可以直接用来定义
2. 类里面进行值传递，要用self。

1. 如果不用静态方法，而又需要一个node，则在__init__初始化一个就可以了。
2. 边界问题。两个List任意出现None的情况，或者长度不够的情况
"""

class Node(object):
    def __init__(self,x):
        self.val = x
        self.next = None
    
class LinkList(object):
    def __init__(self):
        self.head = None
        
        
    def initList(self,values):
        self.head = Node(values[0])
        move = self.head
        
        for v in values[1:]:
            node = Node(v)
            move.next = node
            move = move.next
        
'''
    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = LNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next

'''


class Solution:
    def FindKthToTail(self, head, k):
            if head is None or k < 0 :
                return None
            LinkA = head
            LinkB = head
            
            # 怎么让链表往下走
            for i in range(k):
                if LinkA.next:
                    LinkA = LinkA.next
                else:
                    return None
                
            while(LinkA.next):
                LinkA = LinkA.next
                LinkB = LinkB.next
            
            return LinkB.val
            
                
if __name__ == "__main__":
    #初始化链表与数据
    data = [1,2,3,4,5]
    
    l = LinkList()
    l.initList(data)       

    solution = Solution()
    
    print(solution.FindKthToTail(l.head,2))



'''


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        pAhead = head
        pBehind = None
        for i in range(k-1):
            if pAhead.next:
                pAhead=pAhead.next
            else:
                return None
        pBehind = head
        while pAhead.next:
            pAhead=pAhead.next
            pBehind=pBehind.next
        return pBehind.data


class LNode(object):
    #结点初始化函数, p 即模拟所存放的下一个结点的地址
    #为了方便传参, 设置 p 的默认值为 0 
    def __init__(self, data, p=0):
        self.data = data
        self.next = p


class LinkList(object):
    
    # 属性
    def __init__(self):
        self.head = None

    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = LNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next

    #链表判空
    def isEmpty(self):
        if self.head.next == 0:
            print ("Empty List!")
            return 1
        else:
            return 0

    #取链表长度
    def getLength(self):
        if self.isEmpty():
            exit(0)

        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    #遍历链表
    def traveList(self):
        if self.isEmpty():
            exit(0)
        print ('\rlink list traving result: ',)
        p = self.head
        while p:
            print( p.data,)
            p = p.next

    #链表插入数据函数
    def insertElem(self, key, index):
        if self.isEmpty():
            exit(0)
        if index<0 or index>self.getLength()-1:
            print ("\rKey Error! Program Exit.")
            exit(0)

        p = self.head
        i = 0
        while i<=index:
            pre = p
            p = p.next
            i += 1

        #遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = LNode(key)
        pre.next = node
        node.next = p

    #链表删除数据函数
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index<0 or index>self.getLength()-1:
            print ("\rValue Error! Program Exit.")
            exit(0)

        i = 0
        p = self.head
        #遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i==index:
                pre.next = p.next
                p = None
                return 1

        #p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None

'''



class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k<=0:
            return None
        pAhead=head
        pBehind=None
        for i in range(k-1):
            if pAhead.next:
                pAhead=pAhead.next
            else:
                return None
        pBehind=head
        while pAhead.next:
            pAhead=pAhead.next
            pBehind=pBehind.next
        return pBehind.data




if __name__ == "__main__":
    #初始化链表与数据
    data = [1,2,3,4,5]
    
    l = LinkList()
    l.initList(data)       

    solution = Solution()
    
    while l.head.next:
        print(l.head.data)
        l.head = l.head.next
    
    print(solution.FindKthToTail(l.head,2))

    '''
     
    l.traveList()
    
    #插入结点到索引值为3之后, 值为666
    l.insertElem(666, 3)
    l.traveList()
    
    #删除索引值为4的结点
    l.deleteElem(4)
    l.traveList()
    '''
        









