#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
File: zipString.py

Created on Wed Jan 31 17:35:07 2018

@author: Gsharp

压缩字符 若压缩后长度长于原字符串则舍弃
aaaabbbcccc -> a3b3c4

"""    
def zipString(iniString):
        # write code here
        length = len(iniString)
        if len(iniString) > 2:
           temp = iniString[0]
           t = [temp]
           count = 0
           for item in iniString:
               if item == temp:
                   count += 1
               else:
                   t.append(str(count))
                   temp = item
                   t.append(temp)
                   count = 1
           t.append(str(count))
           if len(t) < length:
                return "".join(t)
           else:
                return iniString
        else :
            return iniString
print zipString("aaaaabbbbc")
def clearZero(mat, n):
        # write code here
        row = []
        column = []
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                   row.append(i)
                   column.append(j)
        for i in row:
            for j in range(n):
                mat[i][j]=0
        for j in column:
            for i in range(n):
                mat[i][j]=0
        return mat
print clearZero([[1,2,3],[0,1,2],[0,0,1]],3)



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        count = 0
        out = head
        while head !=  None:
            head = head.next
            if (count == k):
                out = out.next
            else:
                count += 1
       return out          
        
