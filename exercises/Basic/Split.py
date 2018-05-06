#!/usr/bin/python
# -*- coding=utf-8 -*-
values = input("Input some comma sepreated numbers: ")
list = str(values).split(',')
tuple = tuple(list)
print('list:'+str(list))
print('tuple:'+ str(tuple))
