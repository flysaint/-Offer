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

# 定义空链表数据结构，传入值
class ListNode(object):
    '''
    链表的数据结构
    值
    前后后指针。
    '''
    def __init__(self,x):
        self.val = x
        self.next = None

class Link(object):
    '''
    赋值链表的操作
    1. 初始化头节点
    2. 头结点赋值给一般节点。
    3. 遍历数据赋值给一般节点。
    3.1 初始化临时节点。
    3.2 临时节点赋值给一般节点的后节点
    3.3 一般节点后移。将一般节点的后节点赋值给一般节点。
    '''
    @staticmethod
    def link(values):
        head = ListNode(0)
        move = head
        for v in values:
            node = ListNode(v)
            move.next = node
            move = move.next
        
        return head
        
def print_link_recursion(link):
    '''
    链表打印。
    思路。每次递归找下一个节点，直到没有节点，最后
    '''
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


def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print(links.val)

if __name__ == '__main__':
    head = Link.link([1, 2, 3, 4, 5, 6])
    # print_links(head)
    print_link_recursion(head)
    
'''   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    