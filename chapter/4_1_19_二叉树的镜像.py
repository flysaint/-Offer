#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
04_1_19_mirror_binary_tree

题目：二叉树的镜像

题：操作给定的二叉树，将其变换为源二叉树的镜像。

二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

'''




class TreeNode(object):
    
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
        

def mirror(pRoot):
    
    
    if pRoot is None:
        return 
    
    if pRoot.left is None and pRoot.right is None:
        return 
    
    
    if pRoot is not None:
    
        # 不是交换值，交换指针
        pTmp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = pTmp
        
        if pRoot.left:
            mirror(pRoot.left)
        if pRoot.right:
            mirror(pRoot.right)
    
from collections import namedtuple
from io import StringIO
import math

# define the node structure
Node = namedtuple('Node', ['data', 'left', 'right'])

 
pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10
    


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


if __name__ == '__main__':
    #pretty_print(tree)  
    pretty_print(pRoot1)
    mirror(pRoot1)
    pretty_print(pRoot1)