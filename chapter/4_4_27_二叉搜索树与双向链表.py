# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:11:47 2019

@author: DELL

4_4_27_二叉搜索树与双向链表

题：二叉搜索树与双向链表

题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

解题思路一：由于输入的一个二叉搜索树，其左子树大于右子树的值，
这位后面的排序做了准备，因为只需要中序遍历即可，将所有的节点保存到一个列表，。

对这个list[:-1]进行遍历，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。

借助了一个O（n）的辅助空间 

解题代码：（注意：attr列表中的元素是链表节点）
"""



class tree:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
        
class double_link:
    def __init__(self,x):
        self.data = x
        self.prev = None
        self.next = None

class Solution:
    def mid_traverse(self,root):
        '''
        中序遍历，查看所有节点
        '''
        path_val = []
        path = []
        if root is None:
            return 
        
        def mid_traver(root,path,path_val):
            head = root
            if(head.left):
                mid_traver(head.left,path,path_val)
                
            path.append(head)
            path_val.append(head.data)
            
            if(head.right):
                mid_traver(head.right,path,path_val)
            
        
        mid_traver(root,path,path_val)
        
        return path_val,path
    
    def trans_2_double_linked(self,node_list):
        
        head = double_link(node_list[0])
        head.prev = None
        node = head
        for v in node_list[1:]:
            tmp = double_link(v)
            node.next = tmp
            prev_node = node
            node = node.next
            node.prev = prev_node
        
        return head,node
    
    
    def Convert_1(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.attr=[]
        self.inOrder_1(pRootOfTree)
        
        for i,v in enumerate(self.attr[:-1]):
            self.attr[i].right=self.attr[i+1]
            self.attr[i+1].left=v
        
        return self.attr[0]
    
    def inOrder_1(self,root):
        if not root:
            return
        self.inOrder_1(root.left)
        self.attr.append(root)
        self.inOrder_1(root.right)        
            
            
            
            
            
            
                
        



if __name__ == "__main__":
    
    node1 = tree(12)
    node2 = tree(4)
    node3 = tree(16)
    node4 = tree(3)
    node5 = tree(11)
    node6 = tree(13)
    node7 = tree(18)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    
    #pretty_print(node1)
    s = Solution()
    path_val,path = s.mid_traverse(node1)
    head,node = s.trans_2_double_linked(path_val)
    #print(head)
    #print(node)
    while(node):
        print(node.data)
        node = node.prev
    
    '''
    while(head):
        print(head)
        head = head.next
        
        
    while(node):
        print(node)
        node = node.prev
    '''
















