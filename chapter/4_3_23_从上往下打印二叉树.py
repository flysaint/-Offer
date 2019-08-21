# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:03:39 2019

@author: DELL

4_3_23_从上往下打印二叉树

肯定是递归或者循环


怎么初始化二叉树

定义后手动进行关联，或者先生成节点

"""

from collections import namedtuple
from io import StringIO
import math


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, b):
        self.queue.insert(0, b)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []


def getheight(node):
    if not node:
        return 0
    else:
        return max(getheight(node.left), getheight(node.right)) + 1

def add_padding(str, pad_length_value):
    str = str.strip()
    return str.center(pad_length_value, ' ')

# sotre node , space and slashes in list first, then print out
def pretty_print(tree):
    output = StringIO()
    pretty_output = StringIO()

    current_level = Queue()
    next_level = Queue()
    current_level.enqueue(tree)
    depth = 0

    # get the depth of current tree
    # get the tree node data and store in list
    if tree:
        while not current_level.isEmpty():
            current_node = current_level.dequeue()
            output.write('%s ' % current_node.data if current_node else 'N ')
            next_level.enqueue(
                current_node.left if current_node else current_node)
            next_level.enqueue(
                current_node.right if current_node else current_node)

            if current_level.isEmpty():
                if sum([i is not None for i in next_level.queue]
                       ):  # if next level has node
                    current_level, next_level = next_level, current_level
                    depth = depth + 1
                output.write('\n')
    print('the tree print level by level is :')
    print(output.getvalue())
    print("current tree's depth is %i" % (depth+1))

    # add space to each node
    output.seek(0)
    pad_length = 3
    keys = []
    spaces = int(math.pow(2, depth))

    while spaces > 0:
        skip_start = spaces * pad_length
        skip_mid = (2 * spaces - 1) * pad_length

        key_start_spacing = ' ' * skip_start
        key_mid_spacing = ' ' * skip_mid

        keys = output.readline().split(' ')  # read one level to parse
        padded_keys = (add_padding(key, pad_length) for key in keys)
        padded_str = key_mid_spacing.join(padded_keys)
        complete_str = ''.join([key_start_spacing, padded_str])

        pretty_output.write(complete_str)

        # add space and slashes to middle layer
        slashes_depth = spaces
        print('current slashes depth im_resize:')
        print(spaces)
        print("current levle's list is:")
        print(keys)
        spaces = spaces // 2
        if spaces > 0:
            pretty_output.write('\n')  # print '\n' each level

            cnt = 0
            while cnt < slashes_depth:
                inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                symbol_start_spacing = ' ' * (skip_start-cnt-1)
                symbol_mid_spacing = ' ' * (skip_mid-2*(cnt+1))
                pretty_output.write(''.join([symbol_start_spacing, symbol]))
                for i in keys[1:-1]:
                    pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                pretty_output.write('\n')
                cnt = cnt + 1

    print(pretty_output.getvalue())



class tree(object):
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
        
'''
怎么实现递归

用一个两个list实现。一个放值，一个节点。
每次放进去一个node，然后出列。将值放入值list再把左右孩子放进去。再出列一个，
'''

class Solution():
    
    
    def printTree(self,node):
        # 没有根节点        
        if not node:
            return []
        
        res = []
        res_data = []
        res.append(node)
        while(res):
            node = res.pop(0)
            res_data.append(node.data)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        
        return res_data
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res=[]
        res_val=[]
        res.append(root)
        while len(res)>0:
            node=res.pop(0)
            res_val.append(node.data)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        return res_val

'''
思路：肯定是走递归

一个node节点要设变把左右都遍历


'''


if __name__ == "__main__":
    
    node1 = tree(1)
    node2 = tree(4)
    node3 = tree(5)
    node4 = tree(10)
    node5 = tree(3)
    node6 = tree(8)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    
    s = Solution()
    print(s.printTree(node1))
    pretty_print(node1)
    
    #pretty_print(node1)
    
