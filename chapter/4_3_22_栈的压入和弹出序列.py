# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:23:52 2019

@author: DELL

4_3_22_栈的压入和弹出序列
面试31题：

题目：栈的压入、弹出元素

题：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）


挺难的，比较抽象。可以手写模拟一下。
，一个是压栈，一个是出栈，一个是辅助栈，
把数据从 push向 stack中压，如果压入数据和popv出的棧顶元素一致，
就人从 pushy和popv中同时弹出去，不要往 stack中压了。
等到 pushy中元全弹出来之后，判断 stacki中出栈元素和popv中出栈元素是否一致，
当popv中元素全部弹出，就结束，说明是一致的，手写演示一下就性

入栈1，2，3，4，5出栈4，5，3，2，1

首先1入辅助栈，此时顶1≠4，继续入钱2

此时栈顶3≠4，继续入栈4

此时栈顶4=4，出钱4，弹出序列向后一位，此时为5，，助钱里面是1，2，3

出栈5，準出序列向后一位，此时为3，，辅助钱里面是1，2，3

依次执行，最后輸助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack=[]
        while popV:
            #相当于元素进栈后立即出栈
            if pushV and pushV[0]==popV[0]:
                pushV.pop(0)
                popV.pop(0)
            #如果当前辅助栈中的栈顶元素刚好是要弹出的元素，那么直接弹出
            elif stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
            #不断往辅助栈中压入元素
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True















