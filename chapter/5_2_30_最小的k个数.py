# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:03:39 2019

@author: DELL

5_2_30_最小的k个数


题：输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

先找出第k小的数


"""




    
    
    
def Partition(arr,l,r):
    less = l - 1
    more = r
    
    while(l < more):
        if arr[l] == arr[r]:
            l += 1
        elif arr[l] < arr[r]:
            swap(arr,l,less+1)
            l += 1
            less += 1
        elif arr[l] > arr[r]:
            swap(arr,l,more-1)
            more -= 1
    
    swap(arr,l,r)
    return l

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def GetLeastNumbers(arr,k):
    
    l = 0
    r = random.sample(range(len(arr)),1)[0]
    
    swap(arr,r,len(arr) - 1)
    
    index = Partition(arr,0,len(arr)-1)
    while(index != k):
        if index > k:
            
    
    


import random 
import copy


testArr1 = random.sample(range(20),5)

testArr2 = copy.copy(testArr1)



index = Partition(testArr2,0,len(testArr2) - 1)



















