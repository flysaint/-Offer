# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:41:43 2019

@author: DELL

面试题3： 二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从行到下的递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

思路：二分查找。谁是关键点，对角线的点，右上角和左下角

"""
import numpy as np

testMatrix = [
        [1,2,8,9],
        [2,4,9,12],
        [4,7,10,13],
        [6,8,11,15]
        ]

matrix = testMatrix

testMatrix[3][1]

find_num = 7

def find(matrix,rows,columns,number):

    found_flag = False
    
    if matrix != np.nan and rows > 0 and columns > 0:
        row = 0
        column = columns - 1
        while(row < rows and column >= 0):
            if matrix[row][column] == number:
                found_flag = True
                break
            elif matrix[row][column] > number:
                column -= 1
            else:
                row += 1
    return found_flag
            

print(find(testMatrix,3,3,3))
            


print(find_num(testMatrix,3,3,7))

def find_num(matrix,rows,columns,number):
    find_flag = False
    column = 0
    row = rows - 1
    if matrix != np.nan and rows > 0 and columns > 0:
        while(column < columns and row > 0):
            if matrix[row][column] == number:
                find_flag = True
                return find_flag
            elif matrix[row][column] < number:
                column += 1
            else:
                row -= 1
    return find_flag















            