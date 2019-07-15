# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:46:03 2019

@author: DELL

面试21题：

题目：调整数组的顺序使奇数位于偶数前面

题一：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分。

解题思路：使用两个指针，第一个指针初始化指向数组的第一个数字，从前向后移动，遇到偶数就停下来；
第二个指针指向数组的最后一个数字，从后向前移动，遇到奇数就停下来，交换两个指针指向的元素，直到两个指针相遇。

题二：在题一基础上，要求奇数和奇数，偶数和偶数的相对位置保持不变

"""
import random
import numpy as np

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    

def reOrderArray(arr):

    # 边界要判断和处理下
    i = 0
    j = len(arr) - 1
    while(i < j):
        # 如果是 奇数
        if (np.mod(arr[i],2) == 1):
            i = i + 1 
            continue
        # arr[i] 是偶数了，此时继续遍历j
        # 如果arr[j] 是奇数
        elif(np.mod(arr[j],2) == 0):
            j = j - 1
            continue
        else:
            swap(arr,i,j)
            i = i + 1
            j = j - 1


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if array==None or len(array)==0:
            return
        pBegin=0
        pEnd=len(array)-1
        while (pBegin<pEnd):
            while pBegin<pEnd and not self.isEven(array[pBegin]):
                pBegin += 1
            while pBegin<pEnd and self.isEven(array[pEnd]):
                pEnd -= 1
            if pBegin<pEnd:
                temp=array[pBegin]
                array[pBegin]=array[pEnd]
                array[pEnd]=temp
        return array

    def isEven(self,number):
        return number & 1==0


if __name__ == '__main__':
    arr = random.sample(range(100),5)
    reOrderArray(arr)
    print(arr)
        
        
        
        