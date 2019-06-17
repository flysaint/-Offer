# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:42:09 2019

@author: DELL
题目：数值的整数次方

题：实现函数double Power(double base, int exponent)，求base的exponent次方、不得使用库函数，同时不需要考虑大数问题。
解题思路：主题考虑底数为0.0，指数为负数的情况，此时可以利用全局变量指出g_InvalidInput为True,同时返回0.0

底数为0.0。
返回0，或者1

"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.g_InvalidInput=False
    def Power(self, base, exponent):
        # write code here
        if base==0.0 and exponent<0:
            self.g_InvalidInput=True
            return 0.0
        if exponent>=0:
            return self.PowerWithUnsignedExponent2(base,exponent)
        return 1.0/self.PowerWithUnsignedExponent2(base,-exponent)

    def PowerWithUnsignedExponent2(self, base, exponent):
        if exponent==0:
            return 1
        if exponent==1:
            return base
        # 用 >> 1 替代 除以 2，效率提高
        res=self.PowerWithUnsignedExponent2(base,exponent>>1)
        res *= res
        # 位与运算符替代 % 判读是 奇数还是偶数。效率高很多
        if exponent & 0x1==1:
            res*=base
        return res


if __name__ == '__main__':
    a  = Solution()
    print(a.Power(2,-1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    