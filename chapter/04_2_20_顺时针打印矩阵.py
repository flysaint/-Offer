'''
04_2_20_顺时针打印矩阵

题目：顺时针打印矩阵（同LeetCode 螺旋矩阵打印）

题：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 

则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

个人思路：
肯定和行，列的 标识相关
我在多一个标识记录行列

'''
import numpy as np


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix is None or len(matrix)<=0 or len(matrix[0])<=0:
            return
        start=0
        rows=len(matrix)
        columns=len(matrix[0])
        res=[]
        while(columns > start*2 and  rows > start*2):
            res = self.printMatrixInCircle(matrix,columns,rows,start,res)
            start += 1
            
        return res
    
    def printMatrixInCircle(self,matrix,columns,rows,start,res):
        '''
        # 设置了两个边界
        endX=columns-1-start
        endY=rows-1-start
        ## 规律是start发现了没有，都是从 start或者 row
        
        # 从左到右打印一行
        if start < endX+1:
            for i in range(start,endX+1):
                res.append(matrix[start][i])
        
        # 从上到下打印一列
        if start<endY:
            for i in range(start+1,endY+1):
                res.append(matrix[i][endX])
                
        # 从右到左打印一行
        if start<endX and start<endY:
            for i in range(endX-1,start-1,-1):
                res.append(matrix[endY][i])
                
        # 从下到上打印一列
        if start<endX and start<endY-1:
            for i in range(endY-1,start,-1):
                res.append(matrix[i][start])
        return res
    
        '''
            



if __name__ == '__main__':
    
    test_matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(test_matrix)
        
    s = Solution()
    res_list = s.printMatrix(test_matrix)
    print(res_list)


    
matrix = test_matrix
start=0
rows=len(matrix)
columns=len(matrix[0])
res = []

endX = columns - start 

endY = rows - start

# 第一行
if start < endX - 1:
    for i in range(start,endX):
        res.append(matrix[start][i])

# 最后一列 
if start < endY - 1:
    for i in range(start+1,endY):
        res.append(matrix[i][endX-1])
        

# 最后一行
if start < endY - 1:
    for i in range(endX - 2,start-1,-1):
        res.append(matrix[endY - 1][i])

# 第一列
if start < endY - 1:
    for i in range(endY - 2,start-1,-1):
        res.append(matrix[endY - 1][i])






'''
未完成思路。通过 模拟 行里变化方式，找到共性

row_list = [i for i in range(test_matrix.shape[0])]
col_list = [i for i in range(test_matrix.shape[1])]

        
        
print_list = []

# 第一行
i = 0
j = 0
while(j < (test_matrix.shape[1])):
    print_list.append(test_matrix[i][j])
    j += 1
j -= 1  
  
# 第四列
while(i < (test_matrix.shape[0]) ):
    print_list.append(test_matrix[i][j])
    i += 1
i -= 1    
j -= 1
    
# 第四行
while(j >= 0):
    print_list.append(test_matrix[i][j])
    j -= 1
j += 1
i -= 1

# 第一列
while(j >= 0):
    print_list.append(test_matrix[i][j])
    j -= 1
j += 1

'''




