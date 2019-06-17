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
        把信息利用到极致
        因为有两个数组，两数组。前面的是大数组，后面的是小数组。
        我要找到大数组的最后一个元素。下一个就是最小值。
        '''
        p1 = 0
        p2 = len(arr) - 1
        if arr[p1] > arr[p2]:
            while(p2 - p1 > 1):
                mid = p1 + int((p2 - p1)/2)
                print("p1 = {},p2 ={},mid = {}".format(p1,p2,mid))
                print("arr[p1] = {},arr[p2] = {},arr[mid] = {}".format(arr[p1],arr[p2],arr[mid]))
                if arr[mid] > arr[p1]:
                    p1 = mid
                    continue
                elif arr[mid] < arr[p2]:
                    p2 = mid
                    continue
            return arr[p2]
        else:
            return arr[p1]
        
        
        
        







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