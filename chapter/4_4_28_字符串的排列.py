# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:07:33 2019

@author: DELL

4_4_28_字符串的排列

题：字符串的排列

题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

解题思路：把字符串看成两部分：第一部分是它的第一个字符；第二部分是后面的所有字符。 递归

返回值是什么？怎么和递归直接结合？返回path，还是其他方式
之前是怎么做的？

上次那到题，是遍历所有的组合的可能，是加入进去后再进行删除，可能不太一样.

把第一个字符和后面的字符交换？


思考：
1. 对当前子串进行遍历
2. 将当前子串剔除，递归产生子串 集合
3. 当前剔除的子串和所有集合结合看结果
注意：
1. 集合递归的问题，我是把所有可能都放入了集合内部
2. 两个相同的子串，交换位置他们的

"""

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss)==1:
            return list(ss)
        pStr=[]
        charlist=list(ss)
        # 做排序的目的是什么？
        # 看起来和连续多个字符相等有关系
        
        #charlist.sort()
        
        for i in range(len(charlist)):
            # 这是要干嘛
            #if i>0 and charlist[i]==charlist[i-1]:
            #    continue
            # 这里做了递归
            # 等于没有使用当前字符的情况下，有多少种字符组合
            temp=self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))
            # 这里做了字符串的累加
            for j in temp:
                # 没有当前字串情况下的可能，和当前字符串的所有可能组合
                pStr.append(charlist[i]+j)
        # pStr包含所有可能      
        return pStr




    def Permutation_2(self,strs):
        if strs is None or len(strs) < 1:
            return []
        
        # 中止条件还没说完
        if len(strs) == 1:
            return list(strs)
        
        strs_list = []
        
        for i in range(len(strs)):
            if i < len(strs)-1 and strs[i] == strs[i+1]:
                continue
            
            tmp_list = self.Permutation_2(strs[:i]+strs[i+1:])
            
            for s in tmp_list:
                strs_list.append(strs[i]+s)
        
        return strs_list


    def Permutation_3(self, ss):
        # write code here
        if not ss:
            return []
        
        # 只有一位的情况
        if len(ss)==1:
            return list(ss)
        pStr=[]
     
        # 做排序的目的是什么？
        # 看起来和连续多个字符相等有关系
        
        #charlist.sort()
        
        for i in range(len(ss)):
            # 这是要干嘛
            #if i>0 and charlist[i]==charlist[i-1]:
            #    continue
            # 这里做了递归
            # 等于没有使用当前字符的情况下，有多少种字符组合
            temp=self.Permutation_3(''.join(ss[:i])+''.join(ss[i+1:]))
            # 这里做了字符串的累加
            for j in temp:
                # 没有当前字串情况下的可能，和当前字符串的所有可能组合
                pStr.append(ss[i]+j)
        # pStr包含所有可能      
        return pStr



def Permutation_3(self,strs):
    ## 边界条件
    if strs is None or len(strs) < 1:
        return []
    
    if len(strs) == 1:
        return list(strs)
    
    pStrs = []
    
    for i in range(len(strs)):
        tmp = self.Permutation_3(strs[:i]+strs[i+1:])
        # 将里面所有的和当前做组合
        for s in tmp:
            pStrs.append(tmp+strs[i])
        
    return pStrs
        









if __name__ == '__main__':
    s = Solution()
    strs = 'abc'
    #print(s.Permutation(strs))
    #print(s.Permutation_2(strs))
    print(s.Permutation_3(strs))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    