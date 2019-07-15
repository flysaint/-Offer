# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:09:02 2019

@author: DELL

翻转链表的思路
定义节点
定义链表。静态方法，并且直接返回头结点
递归方法打印。

题目：删除链表中的节点

题一：在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，
定义一个函数在O(1)时间内删除该节点。

解题思路：我们要删除节点i,先把i的下一个节点j的内容复制到i,然后把i的指针指向节点j的下一个节点。
此时再删除节点j,其效果等同于把节点i删除了。

"""

class ListNode:
    def __init__(self):
        self.value = None
        self.next_node = None

class Solution:
    def delete_node(self,head_node,del_node):
        """
        删除指定节点
        """
        if not (head_node and del_node):
            return False

        #要删除的节点不是尾节点
        if del_node.next_node:
            del_next_node=del_node.next_node
            del_node.value=del_next_node.value
            del_node.next_node=del_next_node.next_node
            del_next_node.value=None
            del_next_node.next_node=None
        
        #链表只要一个节点，删除头节点（也是尾节点）
        elif del_node==head_node:
            head_node=None
            del_node = None

        #链表中有多个节点，删除尾节点
        else:
            node=head_node
            while node.next_node!=del_node:
                node=node.next_node
            node.next_node=None
            del_node=None
            
        return head_node