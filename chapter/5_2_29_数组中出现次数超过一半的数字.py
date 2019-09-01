# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:23:30 2019

@author: DELL

5_2_29_数组中出现次数超过一半的数字

题目：数组中出现次数超过一半的数字

题：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

解题思路：根据数组特点找出时间复杂度为O(n)的算法。
因为该数字出现次数比其他所有数字出现的次数之和还要多，所有要找的数字肯定是最后一次把次数设为1时对应的数字。

"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        #检查数组是否为无效的输入
        if not numbers or len(numbers)<=0:
            return 0
        
        #若存在则该数出现次数比其他所有数字出现次数之和还要多，则要找的数字肯定是最后一次把次数设为1时对应的数字
        res=numbers[0]
        times=1
        '''
        这里的目标只是找出了出现次数最多的值？
        
        '''
        for i in range(1,len(numbers)):
            # 如果是第一次出现的值，则更换新值。次数置为1
            # 如果是第n次出现，则times加1
            # 否则，times的次数 -1 。
            # 0换=加，否-法则
            if times==0:
                res=numbers[i]
                times=1
            elif numbers[i]==res:
                times+=1
            else:
                times-=1
                
        #检查其次数是否大于数组的一半，若不是则返回0
        def CheckMoreThanHalf(numbers,number):
            length=len(numbers)
            times=0
            for i in range(length):
                if numbers[i]==number:
                    times+=1
            if times*2<=length:
                return False
            return True
        if CheckMoreThanHalf(numbers,res):
            return res
        return 0
    
    
    def MoreThanHalfNum_Solution_1(self, numbers):
        
        if numbers is None or len(numbers) < 1:
            return False
        
        # 找到出现次数最多值。0换=加否减
        times = 1
        res = numbers[0]
        # 找到出现次数最多的值
        for i in range(1,len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif res == numbers[i]:
                times += 1
            else:
                times -= 1
                
        def ismorethanHalf(numbers,number):
            times = 0
            for i in range(len(numbers)):
                if number == numbers[i]:
                    times += 1
            
            if times >= len(numbers)/2:
                return True
            else:
                return False
            
        if ismorethanHalf(numbers,res):
            return res
        return False    
            
            
            
                
    
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    #nums = [1,2,3,2,2,2,5,4,2]
    nums = [1,2,3,2,1,1,2,2,2]
    print(s.MoreThanHalfNum_Solution_1(nums))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    