# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:14:51 2019

@author: DELL

4_3_21_包含min函数的栈

题目：包含min函数的栈

题：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。在该栈中，调用min、push、pop的时间复杂度都是O(1)

解题思路：
1）如果每次压入新元素时，再调整让新元素位于栈顶，这种思路不能保证最后压入栈的元素最先出栈，因此这个数据结构已经不是栈了。X

2）如果在栈中添加一个成员变量存放最小元素，那么当最小元素弹出后，就不知道下一个最小元素在哪儿了。因此，必须将次小元素保存。X

3）把每次的最小元素保存起来放在另一个辅助栈里。 √

我每次入栈的时候，就把最小元素放起来

形成辅助队列
里面要不要做成有序数组？
1. 要。如果做成有序数组，将来出列的时候，有两个重复值怎么办？那不用数组，使用大根堆，或者小根堆。
2. 不要。只有一个值。进行一次出列，如果是最小值出列，下一个最小值怎么放进去呢？


"""
import  heapq

class stack(object):
    def __init__(self):
        self.stackA = []
        self.stackMin = []
        
    def push(self,x):
        self.stackA.append(x)
        if len(self.stackMin) == 0:
            self.stackMin.append(x)
        else:
            heapq.heappush(self.stackMin,x)
            
            
    def pop(self):
        x = self.stackA.pop()
        self.stackMin.remove(x)
        return x
    
    def get_min(self):
        return self.stackMin[0]


            
        
if __name__ == '__main__':
    
    stackX = stack()
    data = [1,3,5,7,9,2,4,6,8,0]
    for i in data:
        stackX.push(i)
    
            
    
