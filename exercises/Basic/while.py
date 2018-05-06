#!/usr/bin/python
# -*- coding=utf-8 -*-
'''
File: while.py

Created on Thu Feb  1 10:36:07 2018

@author: gsharp

while，if-elif-else 语句的使用

'''
number = 23
running = True

while running:
    guess = int (raw_input('Enter an integer:'))

    if guess == number:
        print 'U Got it!'
        running = False
    elif guess < number:
        print 'higher pls'
    else:
        print 'lower pls'
else:
    print 'the while loop over!'
