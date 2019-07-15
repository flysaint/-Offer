# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:51:05 2019

@author: DELL

面试11题：

题目：
旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

解题思路：二分查找，以及分情况考虑（稍显麻烦）详见：剑指offer P83
"""

class Solution:
    def get_min_numInRotateArr(self,arr):
        '''
        说白了，还是尽量利用数组部分有序的信息。
        折半查找0
        '''
        
        
        L = 0
        R = len(arr) - 1
        
        if(arr[L] < arr[R]):
            return arr[L]
        
        while(L < R):
            mid = L + int((R-L)/2)
            if (arr[mid] > arr[L]):
                L = mid+1
            elif(arr[mid] < arr[R]):
                R = mid-1
            else:
                return arr[mid]
            
        return arr[L]
        

        
        
if __name__ == '__main__':
    testArr = [3,4,5,1,2]
    #testArr = [5,1,2,3,4]
    a = Solution()
    #a.minNumberInRotateArray2(testArr)
    print(a.get_min_numInRotateArr(testArr))
    #print(testArr)        
        




        
        
        







# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return
        if len(rotateArray) == 0:
            return 0
        index1 = 0
        index2 = len(rotateArray) - 1
        indexMid = index1
        while (rotateArray[index1] >= rotateArray[index2]):
            if (index2-index1) == 1:
                indexMid = index2
                break
            indexMid = (index1+index2)//2
            # 如果index1 index2 indexMid三者相等
            if rotateArray[index1]==rotateArray[index2] and rotateArray[indexMid]==rotateArray[index1]:
                return self.minValue(rotateArray,index1,index2)

            if rotateArray[indexMid]>=rotateArray[index1]:
                index1=indexMid
            if rotateArray[indexMid]<=rotateArray[index2]:
                index2=indexMid

        return rotateArray[indexMid]

    def minValue(self,rotateArray,index1,index2):
        res=rotateArray[index1]
        for i in range(index1+1,index2+1):
            if res>rotateArray[i]:
                res=rotateArray[i]
        return res
if __name__ == '__main__':
    #testArr = [1,2,3,4,5]
    testArr = [5,1,2,3,4]
    a = Solution()
    #a.minNumberInRotateArray2(testArr)
    print(a.get_min_numInRotateArr(testArr))
    #print(testArr)