# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:24:51 2019

@author: DELL
4_3_25_二叉树中和为某一值的路径

题目：二叉树中和为某一值的路径

题：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

怎么从根节点遍历二叉树到叶子节点


用递归遍历二叉树的所有路径

1. 路径pop，为什么可以传递出来。在递归中，对path的影响是什么。
"""


class tree:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.data = x


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result=[]
        
        
        
        def FindPathCore(root,path,currentNum,expectNumber):
            currentNum += root.data
            path.append(root)
            # 判断是否达到叶子节点
            flag = (root.left==None and root.right==None)
            
            #如果到达叶子节点且当前值等于期望值
            if currentNum==expectNumber and flag:
                onepath=[]
                for node in path:
                    onepath.append(node.data)
                result.append(onepath)
                
            if currentNum<expectNumber:
                if root.left:
                    FindPathCore(root.left,path,currentNum,expectNumber)
                if root.right:
                    FindPathCore(root.right,path,currentNum,expectNumber)
            path.pop()
                
        FindPathCore(root,[],0,expectNumber)
        return result


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
    
    
    pretty_print(node1)
    s = Solution()
    print(s.FindPath(node1,15))
    

    
    
    
    
    
    
    
    
    
    
    