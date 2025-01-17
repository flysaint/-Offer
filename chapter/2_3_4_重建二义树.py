# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:20:00 2019

@author: DELL

要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值

思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，
00右边是右子树，然后递归的处理左边和右边

提示：二叉树结点，以及对二叉树的各种操作，测试代码见six.py
案例：输入先序遍历 {1,2,4,7,3,5,6,8}中序遍历 {4,7,2,1,5,3,8,6}

重新用树将节点组合起来，返回根节点

学习点。
1. 还是不要忘了递归边界。
2. self可以不用作为参数传入类函数。

先序遍历：根左右
中序遍历：左根右

"""
class Node:
    def __init__(self,x):
        self.data = x
        self.right = None
        self.left = None
        

class Solution:
    def construct_tree(self,preorder=None, inorder=None):
        if not preorder or not inorder:
            return None
        root = Node(preorder[0])
        
        root_index = inorder.index(root.data)
        
        root.left = self.construct_tree(preorder[1:root_index+1],inorder[0:root_index])
        root.right = self.construct_tree(preorder[root_index+1:],inorder[root_index+1:])
        
        return root

'''
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root=TreeNode(pre[0])
        val=tin.index(pre[0])
        
        root.left=self.reConstructBinaryTree(pre[1:val+1],tin[:val])
        root.right=self.reConstructBinaryTree(pre[val+1:],tin[val+1:])
        return root
    

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

'''    
if __name__ == '__main__':
    
    preorder =    [1,2,4,7,3,5,6,8] 
    inorder =    [4,7,2,1,5,3,8,6]   
    s = Solution()
    
    tree = s.construct_tree(preorder,inorder)

    pretty_print(tree)
    
    