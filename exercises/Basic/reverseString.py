#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
File: reverseString.py

Created on Wed Jan 31 18:08:06 2018

@author: gsharp
"""
'''
递归法 反转字符串 不建议使用，递归次数过多
'''
def reverseString(iniString):
    if (len(iniString) > 1):
        return (reverseString(iniString[1:])+iniString[0])
    else :
        return iniString
'''
切片法 极为简便
'''
def reverse(iniString):
    return iniString[::-1]
print(reverseString("123456789"))
print(reverse("123456789"))
