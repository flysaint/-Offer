# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:47:41 2019

@author: DELL
题目：打印从1到最大的n位数

题：输入数字n,按顺序打印出从1到最大的n位十进制数，比如输入3，
则打印出1、2、3一直到最大的3位数999.

解题思路：需要考虑大数问题，这是题目设置的陷阱。可以把问题转换成数字排列问题，用递归让代码更简洁。 
参见剑指offer P114

"""

# -*- coding:utf-8 -*-
class Solution:
    def Print1ToMaxOfNDigits(self, n):
        if n<=0:
            return 
        number=['0']*n
        for i in range(10):
            number[0]=str(i)
            self.Print1ToMaxOfNDigitsRecursively(number,n,0) 
            
    def Print1ToMaxOfNDigitsRecursively(self,number,length,index):
        if index==length-1:
            #self.PrintNumber(number)
            print(''.join(number))
            return
        for i in range(10):
            number[index+1]=str(i)
            self.Print1ToMaxOfNDigitsRecursively(number,length,index+1)
    
    def PrintNumber(self,number):
        #此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        isBeginning0=True
        nLength=len(number)
        for i in range(nLength):
            if isBeginning0 and number[i]!='0':
                isBeginning0=False
            if not isBeginning0:
                print('%c' %number[i])
        print('\t')

    

if __name__=="__main__":
    Solution().Print1ToMaxOfNDigits(2)
    #Solution().Print1ToMaxOfNDigits(3)



'''
def PrintNumber(number):
        #此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        isBeginning0=True
        nLength=len(number)
        for i in range(nLength):
            if isBeginning0 and number[i]!='0':
                isBeginning0=False
            if not isBeginning0:
                print('%c' %number[i])
        print('\t')
        


PrintNumber('123')

'''


def Print1ToMaxOfNDigits(n):
    if n <0:
        return None
    number = ['0']*n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecursively(number,0)
        
    
def Print1ToMaxOfNDigitsRecursively(number,i):
    if i == len(number) - 1:
        print(''.join(number))
        return 
    
    for j in range(10):
        number[i+1] = str(j)
        Print1ToMaxOfNDigitsRecursively(number,i+1)
    
    
    
Print1ToMaxOfNDigits(2)    
    
    


