# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:44:52 2019

@author: DELL

面试题5 从尾到头打印单链表
从尾到头打印单链表
思路1：使用栈
思路2：递归
"""

import numpy as np

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Link:
    @staticmethod
    def link(values):
        head = Node(0)
        move = head
        for v in values:
            node = Node(v)
            move.next = node
            move = move.next
        
        return head.next


# 这里为什么直接用link调用？把Link当做node用
def print_link_recursion(link):
    if link:
        print_link_recursion(link.next)
        print(link.val)

    
if __name__ == '__main__':
    head = Link.link([1, 2, 3, 4, 5, 6])
    # print_links(head)
    print_link_recursion(head)


'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Link(object):

    @staticmethod
    def link(values):
        head = ListNode(0)
        move = head
        try:
            for val in values:
                tmp = ListNode(val)
                move.next = tmp
                move = move.next
        except Exception as e:
            print(e)
        return head.next


def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print(links.val)

if __name__ == '__main__':
    head = Link.link([1, 2, 3, 4, 5, 6])
    # print_links(head)
    print_link_recursion(head)
    
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    