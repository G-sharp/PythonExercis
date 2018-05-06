#!/usr/bin/python
#-*- coding=utf-8 -*-
'''
File: reference.py
Created on Thu Feb  1 10:16:28 2018
@author: gsharp
切片复制法来避免直接引用
'''
print 'Simple Assignment'
shoplist = ['apple','mango','carrot','banana']
mylist = shoplist #简单的赋值 只是引用变量名
del shoplist[0]
del mylist[0]
print 'shoplist is',shoplist
print 'mylist is',mylist

print 'Coping by making full slice'
mylist = shoplist[:]
del mylist[0]
print 'shoplist is',shoplist
print 'mylist is',mylist
